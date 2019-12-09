"""
Functions for plotting the folium maps that users chose in the interface.
For example, they may choose to view clusters or layers, or all the data
marked directly on the map.
(Note not all these choices have been coded into the interface.py yet)
"""

import warnings
import folium
import folium.plugins
from . import mapping_funcs
warnings.filterwarnings('ignore')
import pandas as pd

class Maps:

    """Class encompassing all the functions for generating maps based on user
    selections."""

    def basic_map(
            self, county_name, county, group, dataframe, subgrp_df, map_sink=None):
        """Creates a map with no layers or clusters, the chosen incident_type
        is marked directly on the map at the lat/lon location that it occurs."""

        severity_dict = mapping_funcs.INCIDENT_DICT

        if map_sink is None:
            map_dir = mapping_funcs.MAPS_DIR
            map_sink = map_dir + f'/{county_name}_{group}_basic_map.html'

        # create map object centered at the median location of the df
        lat = dataframe['lat'].median()
        lon = dataframe['lon'].median()

        acc_wa = folium.Map([lat, lon],
                            prefer_canvas=True,
                            zoom_start=8)

        for _, row in subgrp_df.iterrows():
            assert row.COUNTY == county
            # define circle color by severity
            if row.REPORT == 2:
                # injury
                cirlecolor = "#007849" 
            elif row.REPORT == 3: 
                # fatal
                cirlecolor = 'red'
            else:
                # just property damage
                cirlecolor = 'steelblue'

            # define circle radius by severity
            if row.REPORT == 1:
                # property
                cirleradius = 4
            elif row.REPORT == 2:
                # injury
                cirleradius = 8
            else:
                # fatal
                cirleradius = 12

            folium.CircleMarker([row.lat, row.lon],
                                radius=cirleradius,
                                popup=folium.Popup("{}, {}".format(row.FORM_REPT_NO,
                                                                   severity_dict[row.REPORT]), max_width=150),
                                # fill_color="#3db7e4",
                                # color=cirlcolor,
                                weight=0.2,
                                fill_color=cirlecolor,
                                fill=True,
                                fill_opacity=0.4
            ).add_to(acc_wa)

        acc_wa.save(map_sink)

        return acc_wa


    def plot_folium_filtered_clusters(
            self, county_name, county, group, dataframe, subgrp_df, map_sink=None):
        """Create a map with interactable clusters that describes the frequency
        of the chosen incident_type by location."""

        severity_dict = mapping_funcs.INCIDENT_DICT
        
        if map_sink is None:
            map_dir = mapping_funcs.MAPS_DIR
            map_sink = map_dir + f'/{county_name}_{group}_cluster_map.html'

        # create map object centered at the median location of the df
        lat = dataframe['lat'].median()
        lon = dataframe['lon'].median()

        acc_wa = folium.Map([lat, lon],
                            prefer_canvas=True,
                            zoom_start=8)

        clust = folium.plugins.MarkerCluster()

        for _, row in subgrp_df.iterrows():
            if row.REPORT == 2:
                # injury
                cirlecolor = "#007849" 
            elif row.REPORT == 3: 
                # fatal
                cirlecolor = 'red'
            else:
                # just property damage
                cirlecolor = 'steelblue'

            # define circle radius by severity
            if row.REPORT == 1:
                # property
                cirleradius = 4
            elif row.REPORT == 2:
                # injury
                cirleradius = 8
            else:
                # fatal
                cirleradius = 12
                # cirlradius = max(row['# INJ'], row['# FAT']) * 3

            clust.add_child(folium.Marker(
                    location=[row['lat'], row['lon']],
                    radius=cirleradius,
                    popup=folium.Popup("{}: {}".format(
                        row.FORM_REPT_NO,
                        severity_dict[row.REPORT]),
                        max_width=150),
                    weight=0.2,
                    fill_color=cirlecolor,
                    fill=True,
                    fill_opacity=0.4))
        acc_wa.add_child(clust)

        acc_wa.save(map_sink)

        return acc_wa

    def plot_folium_filtered_layers(self, group, county_name, county, grp_feature, subgrp_feature, map_sink=None):
        """Creates a map with layers showing the selected incident_type by
        year."""
        
        datadir = mapping_funcs.DATA_DIR
        severity_dict = mapping_funcs.INCIDENT_DICT

        if map_sink is None:
            map_dir = mapping_funcs.MAPS_DIR
            map_sink = map_dir + f'/{county_name}_{group}_by_year_map.html'
        
        # read data
        dataframe = pd.read_csv(datadir + '/2013.csv')
        dataframe = dataframe[dataframe.COUNTY == county]
        acc_wa = folium.Map([dataframe.lat.median(), dataframe.lon.median()],
                           tiles='',
                           prefer_canvas=True,
                           zoom_start=8)

        folium.TileLayer('cartodbpositron', name='bright').add_to(acc_wa)
        layers = []

        for year in range(2013, 2018):
            
            layer = folium.FeatureGroup(name=str(year), show=False)
            layers.append(layer)
            acc_wa.add_child(layers[-1])
            
            dataframe = pd.read_csv(datadir + '/{}.csv'.format(year))
            dataframe = dataframe[dataframe.COUNTY == county]
            group_df = dataframe.groupby(grp_feature)
            subgrp_df = group_df.apply(lambda g: g[g['weather'] == subgrp_feature])
        
            # add crash events to their layers
            for _, row in subgrp_df.iterrows():
            
                assert row.COUNTY == county
                # define circle color by severity
                if row.REPORT == 2:
                    # injury
                    cirlecolor = "#007849" 
                elif row.REPORT == 3: 
                    # fatal
                    cirlecolor = 'red'
                else:
                    # just property damage
                    cirlecolor = 'steelblue'

                # define circle radius by severity
                if row.REPORT == 1:
                    # property
                    cirleradius = 4
                elif row.REPORT == 2:
                    # injury
                    cirleradius = 8
                else:
                    # fatal
                    cirleradius = 12

                folium.CircleMarker([row.lat, row.lon],
                                    radius=cirleradius,
                                    popup=folium.Popup("{}, {}".format(row.FORM_REPT_NO,
                                                                       severity_dict[row.REPORT]), max_width=150),
                                    weight=0.2,
                                    fill_color=cirlecolor,
                                    fill=True,
                                    fill_opacity=0.4
                ).add_to(layers[-1])

        # add layer control
        folium.LayerControl().add_to(acc_wa)
            
        # save map
        acc_wa.save(map_sink)
    
        return acc_wa


    def plot_folium_filtered_clusters_layers(
            self, county_name, county, group, grp_feature, subgrp_feature,
            map_sink=None):
        """Creates a map with layers showing the selected incident_type by
        year grouped into clusters by region."""

        datadir = mapping_funcs.DATA_DIR
        severity_dict = mapping_funcs.INCIDENT_DICT

        if map_sink is None:
            map_dir = mapping_funcs.MAPS_DIR
            map_sink = map_dir + f'/{county_name}_{group}_cluster_by_year_map.html'
        
        # read data
        dataframe = pd.read_csv(datadir + '/2013.csv')
        dataframe = dataframe[dataframe.COUNTY == county]
        acc_wa = folium.Map([dataframe.lat.median(), dataframe.lon.median()],
                           tiles='',
                           prefer_canvas=True,
                           zoom_start=8)

        folium.TileLayer('cartodbpositron', name='bright').add_to(acc_wa)
        layers = []

        for year in range(2013, 2018):
            
            layer = folium.FeatureGroup(name=str(year), show=False)
            layers.append(layer)
            acc_wa.add_child(layers[-1])
            
            dataframe = pd.read_csv(datadir + '/{}.csv'.format(year))
            dataframe = dataframe[dataframe.COUNTY == county]
            group_df = dataframe.groupby(grp_feature)
            subgrp_df = group_df.apply(lambda g: g[g['weather'] == subgrp_feature])
            
            clust = folium.plugins.MarkerCluster()

            for _, row in subgrp_df.iterrows():
            
                assert row.COUNTY == county
                # define circle color by severity
                if row.REPORT == 2:
                    # injury
                    cirlecolor = "#007849" 
                elif row.REPORT == 3: 
                    # fatal
                    cirlecolor = 'red'
                else:
                    # just property damage
                    cirlecolor = 'steelblue'

                # define circle radius by severity
                if row.REPORT == 1:
                    # property
                    cirleradius = 4
                elif row.REPORT == 2:
                    # injury
                    cirleradius = 8
                else:
                    # fatal
                    cirleradius = 12

                clust.add_child(folium.Marker(
                    location=[row['lat'], row['lon']],
                    radius=cirleradius,
                    popup=folium.Popup("{}, {}".format(row.FORM_REPT_NO,
                                                       severity_dict[row.REPORT]), max_width=150),
                    weight=0.2,
                    fill_color=cirlecolor,
                    fill=True,
                    fill_opacity=0.4)).add_to(layers[-1])

        # add layer control
        folium.LayerControl().add_to(acc_wa)

        # save map
        acc_wa.save(map_sink)

    def plot_folium(self, feature, data, map_sink=None):
        '''Creates a very large map with layers, generates data for all
        possible groups. Will probably remove this map as it isn't really
        useful for our usecases.
        @param data: dataframe wrangled for selected feature
        @param map_sink: saving destination of generated map
        '''
        grouping = data.groupby(feature)
        grp_dict = mapping_funcs.GRP_DICT

        if map_sink is None:
            map_dir = mapping_funcs.MAPS_DIR
            group = grp_dict[feature]
            map_sink = map_dir + f'/{group}_big_map.html'

        # store the different features
        groups = []
        for group in grouping:
            groups.append(group)

        lat = data['lat'].median()
        lon = data['lon'].median()
        # create map object
        acc_wa = folium.Map([lat, lon],
                            # tiles="cartodbpositron",
                            tiles='',
                            # width='80%',
                            # height='80%',
                            prefer_canvas=True,
                            zoom_start=8)
        # add tile layer
        folium.TileLayer('cartodbpositron', name='bright').add_to(acc_wa)
        folium.TileLayer('CartoDB dark_matter', name='dark').add_to(acc_wa)

        # create crash layer
        crashes = []

        # individual crashes
        crash = folium.FeatureGroup(name=feature + '_Crashes', show=False)
        crashes.append(crash)
        acc_wa.add_child(crashes[-1])

        for group in groups:
            for _, row in data[data[feature] == group].iterrows():
                # group is the grouped weather condition
                if row['# INJ'] > 0:
                    cirlcolor = "#007849"
                elif row['# FAT'] > 0:
                    cirlcolor = 'red'
                else:
                    cirlcolor = 'steelblue'

                # define circle radius
                if row['# INJ'] + row['# FAT'] > 0:
                    cirlradius = max(row['# INJ'], row['# FAT']) * 3
                else:
                    cirlradius = 1

                folium.CircleMarker([row['Latitude'], row['Longitude']],
                                    radius=cirlradius,
                                    popup=folium.Popup("INJ: {}, FAT: {}".format(
                                        row['# INJ'], row['# FAT']), max_width=150),
                                    weight=0.2,
                                    fill_color=cirlcolor,
                                    fill=True,
                                    fill_opacity=0.4).add_to(crashes[-1])

        # add layer control
        folium.LayerControl().add_to(acc_wa)

        # save map
        acc_wa.save(map_sink)

        return acc_wa

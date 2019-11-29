import os
import pandas as pd
import folium
import folium.plugins
import numpy as np
from . import mapping_funcs
import warnings
warnings.filterwarnings('ignore')

class Maps:
    
    """Functions for plotting the folium maps that users chose in the interface.
    For example, they may choose to view clusters or layers, or all the data 
    marked directly on the map.
    (Note not all these choices have been coded into the interface.py yet)"""

    def basic_map(self, grp_feature, subgrp_feature, incident_type, df, map_sink = None):

        group_df = df.groupby(grp_feature)
        subgrp_df = group_df.get_group(subgrp_feature)
        r_incident_dict = mapping_funcs.r_incident_dict
        incident = r_incident_dict[incident_type]
        grp_dict = mapping_funcs.grp_dict
        
        if map_sink is None:
            map_dir = mapping_funcs.MAPS_DIR
            group = grp_dict[grp_feature]
            map_sink =  map_dir + f'/{group}_{incident}_basic_map.html'
        
        # create map object centered at the median location of the df
        lat = df['Latitude'].median()
        lon = df['Longitude'].median()
        
        accWA = folium.Map([lat, lon],
                           prefer_canvas=True,
                           zoom_start=8)
    
        for _, row in subgrp_df.iterrows():

            if row[incident_type] > 0:
                cirlColor = "#007849" 
            
                cirlRadius = row[incident_type] * 1.5
            
                folium.CircleMarker(
                    [row['Latitude'], row['Longitude']],
                    radius = cirlRadius,
                    weight = 0.2,
                    fill_color = cirlColor,
                    fill = True,
                    fill_opacity = 0.8,
                    popup = f'{incident},{row[incident_type]}'
                ).add_to(accWA)
                  
        accWA.save(map_sink)
    
        return accWA
    
    
    def plot_folium_filtered_clusters(
        self, grp_feature, subgrp_feature, incident_type, df, 
        map_sink = None):
        
        group_df = df.groupby(grp_feature)
        subgrp_df = group_df.get_group(subgrp_feature)
        r_incident_dict = mapping_funcs.r_incident_dict
        incident = r_incident_dict[incident_type]
        grp_dict = mapping_funcs.grp_dict
        
        if map_sink is None:
            map_dir = mapping_funcs.MAPS_DIR
            group = grp_dict[grp_feature]
            map_sink =  map_dir + f'/{group}_{incident}_cluster_map.html'
        
        # create map object centered at the median location of the df
        lat = df['Latitude'].median()
        lon = df['Longitude'].median()
        
        accWA = folium.Map([lat, lon],
                        # tiles="cartodbpositron",
                        # tiles = '',
                        # width='80%',
                        # height='80%',
                        prefer_canvas=True,
                        zoom_start=8)
    
        clust = folium.plugins.MarkerCluster()
        
        for _, row in subgrp_df.iterrows():
            if row[incident_type] > 0:
                cirlColor = "#007849" 
                cirlRadius = row[incident_type] * 10
                clust.add_child(folium.Marker(
                    location = [row['Latitude'], row['Longitude']],
                    radius=cirlRadius,
                    popup=folium.Popup("{}: {}".format(
                        incident, row[incident_type]), max_width=150),
                    weight = 0.2,
                    fill_color=cirlColor,
                    fill=True,
                    fill_opacity=0.4))

        accWA.add_child(clust)

        accWA.save(map_sink)
    
        return accWA

    def plot_folium_filtered_layers(
        self, grp_feature, subgrp_feature, incident_type, df, 
        map_sink = None):
        
        group_df = df.groupby(grp_feature)
        subgrp_df = group_df.get_group(subgrp_feature)
        r_incident_dict = mapping_funcs.r_incident_dict
        incident = r_incident_dict[incident_type]
        grp_dict = mapping_funcs.grp_dict
        
        if map_sink is None:
            map_dir = mapping_funcs.MAPS_DIR
            group = grp_dict[grp_feature]
            map_sink =  map_dir + f'/{group}_{incident}_layer_map.html'
        
        # create map object centered at the median location of the df
        lat = df['Latitude'].median()
        lon = df['Longitude'].median()
        
        accWA = folium.Map([lat, lon],
                        # tiles="cartodbpositron",
                        tiles = '',
                        # width='80%',
                        # height='80%',
                        prefer_canvas=True,
                        zoom_start=8)

        # add tile layer
        folium.TileLayer('openstreetmap').add_to(accWA)
        #folium.TileLayer('CartoDB dark_matter', name = 'dark').add_to(accWA)

        start = 2008
        end = 2017
        layers = []

        for year in range(start, end + 1):
            layer = folium.FeatureGroup(
                name=str(year) + ': ' + incident, show=False)
            layers.append(layer)
            accWA.add_child(layers[-1])

            for _, row in subgrp_df[subgrp_df['Year'] == str(year)].iterrows():
                
                if row[incident_type] > 0:
                    cirlColor = "#007849" 
            
                    cirlRadius = row[incident_type] * 3
            
                    folium.CircleMarker(
                        [row['Latitude'], row['Longitude']],
                        radius=cirlRadius,
                        weight = 0.2,
                        fill_color=cirlColor,
                        fill=True,
                        fill_opacity=0.8,
                        popup = f'{incident},{row[incident_type]}'
                    ).add_to(layers[-1])

        # add layer control
        folium.LayerControl().add_to(accWA)
        
        # save map
        map_dir = mapping_funcs.MAPS_DIR
        mpsv =  map_dir + f'/{grp_feature}_{incident}_layer_map.html'
        accWA.save(map_sink)
    
        return accWA
    
    
    def plot_folium(self, feature, df, map_sink = None):
        '''
        @param df: dataframe wrangled for selected feature
        @param map_sink: saving destination of generated map
        '''
        grouping = df.groupby(feature)
        grp_dict = mapping_funcs.grp_dict
        
        if map_sink is None:
            map_dir = mapping_funcs.MAPS_DIR
            group = grp_dict[grp_feature]
            map_sink =  map_dir + f'/{group}_{incident}_big_map.html'

        # store the different features
        groups = []
        for group, i in grouping:
            groups.append(group)

        lat = df['Latitude'].median()
        lon =  df['Longitude'].median()
        # create map object
        accWA = folium.Map([lat, lon],
                       # tiles="cartodbpositron",
                       tiles = '',
                       # width='80%',
                       # height='80%',
                       prefer_canvas=True,
                       zoom_start=8)
        # add tile layer
        folium.TileLayer('cartodbpositron', name = 'bright').add_to(accWA)
        folium.TileLayer('CartoDB dark_matter', name = 'dark').add_to(accWA)

        # create crash layer
        crashes = []

        # individual crashes
        crash = folium.FeatureGroup(name=feature + '_Crashes', show=False)
        crashes.append(crash)
        accWA.add_child(crashes[-1])

        for group in groups:
            for _, row in df[df[feature] == group].iterrows():
                # group is the grouped weather condition
                if row['# INJ'] > 0:
                    cirlColor = "#007849" 
                elif row['# FAT'] > 0: 
                    cirlColor = 'red'
                else:
                    cirlColor = 'steelblue'

                # define circle radius
                if row['# INJ'] + row['# FAT'] > 0:
                    cirlRadius = max(row['# INJ'], row['# FAT']) * 3
                else:
                    cirlRadius = 1

                folium.CircleMarker([row['Latitude'], row['Longitude']],
                                    radius=cirlRadius,
                                    popup=folium.Popup("INJ: {}, FAT: {}".format(
                                    row['# INJ'], row['# FAT']), max_width=150),
                                    weight = 0.2,
                                    fill_color=cirlColor,
                                    fill=True,
                                    fill_opacity=0.4
                            ).add_to(crashes[-1])

        # add layer control
        folium.LayerControl().add_to(accWA)

        # save map
        accWA.save(map_sink)

        return accWA

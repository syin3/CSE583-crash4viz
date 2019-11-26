import os
import pandas as pd
import folium
import folium.plugins
import numpy as np

class Maps:
    
    """Functions for plotting the folium maps that users chose in the interface.
    For example, they may choose to view clusters or layers, or all the data 
    marked directly on the map.
    (Note not all these choices have been coded into the interface.py yet)"""
    
    
    def plot_folium_filtered_clusters(
        self, grp_feature, subgrp_feature, incident_type, df, 
        map_sink = 'MyMaps/test_filt.html'):
        
        group_df = df.groupby(grp_feature)
        subgrp_df = group_df.get_group(subgrp_feature)
        
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
    
        clusters = []
        clust = folium.FeatureGroup(name=str(incident_type) + '_Clusters', show=False)
        clusters.append(clust)
        accWA.add_child(clusters[-1])
        
        # add cluster layer to feature group
        marClst = folium.plugins.FastMarkerCluster(
            data=list(zip(subgrp_df['Latitude'], subgrp_df['Longitude']))
        ).add_to(clusters[-1])
        
        for _, row in subgrp_df.iterrows():
            if row[incident_type] > 0:
                cirlColor = "#007849" 
            else:
                cirlColor = 'steelblue'
            
            cirlRadius = np.max(row[incident_type]) * 5
            
            folium.CircleMarker([row['Latitude'], row['Longitude']],
                                        radius=cirlRadius,
                                        popup=folium.Popup("{}: {}".format(incident_type,
                                        row[incident_type]), max_width=150),
                                        weight = 0.2,
                                        fill_color=cirlColor,
                                        fill=True,
                                        fill_opacity=0.4)
                            
        # save map
        accWA.save(map_sink)
    
        return accWA
    
    
    def plot_folium(self, feature, df, map_sink = 'MyMaps/test.html'):
        '''
        @param df: dataframe wrangled for selected feature
        @param map_sink: saving destination of generated map
        '''
        grouping = df.groupby(feature)

        # store the different features
        groups = []
        for group, i in grouping:
            groups.append(group)

        # create map object
        accWA = folium.Map([df['Latitude'].median(), df['Longitude'].median()],
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
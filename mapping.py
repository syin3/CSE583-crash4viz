import os
import pandas as pd
import folium
import numpy as np

class Maps:
    
    def clean_dataframe(self):
        coords = pd.read_csv("data/coords_gps.csv")
        crashes = pd.read_csv("data/WA_Rural_St_RtesCrashes_Full.csv")
        # change the coordinates to be regular lat/lon
        crashes = crashes[crashes["WA STATE PLANE SOUTH - X 2010 - FORWARD"].notnull()].reset_index()
        crashes['Latitude'] = np.array(coords['Latitude'])
        crashes['Longitude'] = np.array(coords['Longitude'])
        # filter for general columns of interest
        crash_df = crashes.filter(["COUNTY", "MOST SEVERE INJURY TYPE", "WEATHER", "ROADWAY SURFACE CONDITION", "LIGHTING CONDITION", "JUNCTION RELATIONSHIP", "# INJ", "# FAT", "# VEH", "# PEDS", "# BIKES", "Latitude", "Longitude"])
        return crash_df
        
    def plot_folium(self, feature, map_sink = 'MyMaps/test.html'):
        '''
        @param df: dataframe wrangled for selected feature
        @param map_sink: saving destination of generated map
        '''
        df = Maps.clean_dataframe(self)
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
#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import folium
import folium.plugins
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import rc

# REPORT (accident severity)
severity_dict = {1: 'Property Damage Only', 2: 'Injury Accident', 3: 'Fatal Accident'}

# weather (weather condition)
# np.nan: 'Unknown'
weather_dict = {0.0: 'Unknown', 1.0: 'Clear or Partly Cloudy',  
                2.0: 'Overcast', 3.0: 'Raining', 4.0: 'Snowing',
                5.0: 'Fog/Smog/Smoke', 6.0: 'Sleet/Hail/Freezing Rain',
                7.0: 'Severe Crosswind', 8.0: 'Blowing Sand or Dirt or Snow',
                9.0: 'Other', 10.0: 'Foggy'}

# LIGHT (lighting condition)
# np.nan: 'Unknown'
light_dict = {1.0: 'Daylight', 2.0: 'Dawn', 3.0: 'Dusk',
              4.0: 'Dark, Street Lights On', 5.0: 'Dark, Street Lights Off', 
              6.0: 'No Street Lights', 7.0: 'Other', 9.0: 'Unknown'}

# COUNTY (county where the accident happened)
county_dict = {0: 'Not Stated', 1:'Adams', 2: 'Asotin', 3: 'Benton', 4: 'Chelan',
               5: 'Clallam', 6: 'Clark', 7:'Columbia', 8: 'Cowlitz', 9: 'Douglas', 
               10: 'Ferry', 11: 'Franklin', 12: 'Garfield', 13: 'Grant', 14: 'Grays Harbor',
               15: 'Island', 16: 'Jefferson', 17: 'King', 18: 'Kitsap', 19: 'Kittitas',
               20: 'Klickitat', 21: 'Lewis', 22: 'Lincoln', 23: 'Mason', 24: 'Okanogan',
               25: 'Pacific', 26: 'Pend Oreille', 27: 'Pierce', 28: 'San Juan',
               29: 'Skagit', 30: 'Skamania', 31: 'Snohomish', 32: 'Spokane',
               33: 'Stevens', 34: 'Thurston', 35: 'Wahkiakum', 36: 'Walla Walla',
               37: 'Whatcom', 38: 'Whitman', 39: 'Yakima'}

# WEEKDAY (day of the week)
weekday_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday',
                6: 'Saturday', 7: 'Sunday'}

rur_urb_dict = {'R': 'rural', 'U': 'urban'}

roadway_surf_dict = {1.0: 'Dry', 2.0: 'Wet', 3.0: 'Snow/Slush', 4.0: 'Ice',
                     5.0: 'Sand/Mud/Dirt', 6.0: 'Oil', 7.0: 'Standing Water',
                     8.0: 'Other', 9.0: 'Unknown'}

def plot_basic(year, county, map_sink):
    """
    basic plot
    @test:
        (1) year, county, map_sink cannot be None
    """

    df = pd.read_csv('../data/crash-merged/{}.csv'.format(year))
    df = df[df.COUNTY == county]
    accWA = folium.Map([df.lat.median(), df.lon.median()],
                   tiles = '',
                   prefer_canvas=True,
                   zoom_start=10)
    folium.TileLayer('cartodbpositron', name = 'bright').add_to(accWA)

    for _, row in df.iterrows():
        assert row.COUNTY == county
        # define circle color by severity
        if row.REPORT == 2:
            # injury
            cirleColor = "#007849" 
        elif row.REPORT == 3: 
            # fatal
            cirleColor = 'red'
        else:
            # just property damage
            cirleColor = 'steelblue'

        # define circle radius by severity
        if row.REPORT == 1:
            # property
            cirleRadius = 4
        elif row.REPORT == 2:
            # injury
            cirleRadius = 8
        else:
            # fatal
            cirleRadius = 12
        # cirlRadius = max(row['# INJ'], row['# FAT']) * 3

        folium.CircleMarker([row.lat, row.lon],
                            radius=cirleRadius,
                            popup=folium.Popup("{}, {}".format(row.FORM_REPT_NO,
                                                               severity_dict[row.REPORT]), max_width=150),
                            # fill_color="#3db7e4",
                            # color=cirlColor,
                            weight = 0.2,
                            fill_color=cirleColor,
                            fill=True,
                            fill_opacity=0.4
                     ).add_to(accWA)
    
    accWA.save(map_sink)
    return accWA

# _ = plot_basic(2017, 18, "test.html")

def plot_layer_by_year(county, map_sink):
    """
    with specified county
    @test:
        (1) county, map_sink cannot be None
    """

    # read data
    df = pd.read_csv('../data/crash-merged/2013.csv')
    accWA = folium.Map([df.lat.median(), df.lon.median()],
                   tiles = '',
                   prefer_canvas=True,
                   zoom_start=8)
    folium.TileLayer('cartodbpositron', name = 'bright').add_to(accWA)

    # add tile layer
    folium.TileLayer('cartodbpositron', name = 'bright').add_to(accWA)
    folium.TileLayer('CartoDB dark_matter', name = 'dark').add_to(accWA)
    
    # create crash layer
    crashes = []
    for year in range(2013, 2018):
        
        df = pd.read_csv('../data/crash-merged/{}.csv'.format(year))
        df = df[df.COUNTY == county]
        
        # individual crashes
        yrCrash = folium.FeatureGroup(name=str(year) + '_Crashes', show=False)
        crashes.append(yrCrash)
        accWA.add_child(crashes[-1])
        
        # add crashe events to their layers
        for _, row in df.iterrows():
            
            assert row.COUNTY == county
            # define circle color by severity
            if row.REPORT == 2:
                # injury
                cirleColor = "#007849" 
            elif row.REPORT == 3: 
                # fatal
                cirleColor = 'red'
            else:
                # just property damage
                cirleColor = 'steelblue'

            # define circle radius by severity
            if row.REPORT == 1:
                # property
                cirleRadius = 4
            elif row.REPORT == 2:
                # injury
                cirleRadius = 8
            else:
                # fatal
                cirleRadius = 12
            # cirlRadius = max(row['# INJ'], row['# FAT']) * 3

            folium.CircleMarker([row.lat, row.lon],
                                radius=cirleRadius,
                                popup=folium.Popup("{}, {}".format(row.FORM_REPT_NO,
                                                                   severity_dict[row.REPORT]), max_width=150),
                                # fill_color="#3db7e4",
                                color='black',
                                weight = 0.2,
                                fill_color=cirleColor,
                                fill=True,
                                fill_opacity=0.2
                         ).add_to(crashes[-1])
    
        

    # add layer control
    folium.LayerControl().add_to(accWA)
            
    # save map
    accWA.save(map_sink)
    
    return accWA

# _ = plot_layer_by_year(17, "test.html")

def plot_cluster(map_sink):
    """
    for cluster
    @test:
        (1) map_sink cannot be None
    """
    
    # start the map at roughly the center of WA state
    accWA = folium.Map([47.303495, -120.819109],
                   tiles = '',
                   prefer_canvas=True,
                   zoom_start=8)
    folium.TileLayer('cartodbpositron', name = 'bright').add_to(accWA)

    # add tile layer
    folium.TileLayer('cartodbpositron', name = 'bright').add_to(accWA)
    folium.TileLayer('CartoDB dark_matter', name = 'dark').add_to(accWA)
    
    # create crash layer
    crashes = []
    clusters = []
    for year in range(2013, 2018):
        
        df = pd.read_csv('../data/crash-merged/{}.csv'.format(year))
        
        # create cluster layer
        yrClust = folium.FeatureGroup(name=str(year) + '_Clusters', show=False)
        clusters.append(yrClust)
        accWA.add_child(clusters[-1])

        # add cluster layer to feature group
        marClst = folium.plugins.FastMarkerCluster(
            data=list(zip(df.lat.values, df.lon.values))
        ).add_to(clusters[-1])
        

    # add layer control
    folium.LayerControl().add_to(accWA)
            
    # save map
    accWA.save(map_sink)
    
    return accWA

# _ = plot_cluster("test.html")

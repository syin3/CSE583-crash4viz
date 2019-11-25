import os
import pandas as pd
import folium
import numpy as np

# all possible variables, {label in dataframe: label in GUI}

vars_dict = {}
vars_dict['WEATHER'] = 'Weather'
vars_dict['ROADWAY SURFACE CONDITION'] = 'Surface Condition'
vars_dict['LIGHTING CONDITION'] = 'Lighting Condition'
vars_dict['JUNCTION RELATIONSHIP'] = 'Junction Relationship'
vars_dict['TIME'] = 'Time'

subgroups_dict = {}
subgroups_dict['Weather'] = ['Blowing Sand or Dirt or Snow', 'Clear or Partly Cloudy', 'Fog or Smog or Smoke', 'Other', 'Overcast','Raining', 'Severe Crosswind', 'Sleet or Hail or Freezing Rain', 'Snowing', 'Unknown']
subgroups_dict['Surface Condition'] = ['Dry', 'Ice', 'Oil', 'Other', 'Sand/Mud/Dirt', 'Snow/Slush', 'Standing Water', 'Unknown', 'Wet']
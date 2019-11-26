import os
import pandas as pd
import folium
import numpy as np

"""Common variables and functions that will be called by mapping.py"""


# all possible variables, {label in dataframe: label in GUI}
vars_dict = {}
vars_dict['Weather'] = 'WEATHER'
vars_dict['Surface Condition'] = 'ROADWAY SURFACE CONDITION'
vars_dict['Lighting Condition'] = 'LIGHTING CONDITION'
vars_dict['Junction Relationship'] = 'JUNCTION RELATIONSHIP'
#vars_dict['TIME'] = 'Time'

incident_dict = {}
incident_dict['Injuries'] = '# INJ'
incident_dict['Fatalities'] = '# FAT'
incident_dict['Number of Vehicles Involved'] = '# VEH'

subgroups_dict = {}
subgroups_dict['Weather'] = [
    'Blowing Sand or Dirt or Snow', 
    'Clear or Partly Cloudy', 
    'Fog or Smog or Smoke', 
    'Other', 
    'Overcast',
    'Raining', 
    'Severe Crosswind', 
    'Sleet or Hail or Freezing Rain', 
    'Snowing', 
    'Unknown']
subgroups_dict['Surface Condition'] = [
    'Dry', 
    'Ice', 
    'Oil', 
    'Other', 
    'Sand/Mud/Dirt', 
    'Snow/Slush', 
    'Standing Water', 
    'Unknown', 
    'Wet']
subgroups_dict['Lighting Condition'] = [
    'Dark-No Street Lights', 
    'Dark-Street Lights Off', 
    'Dark-Street Lights On', 
    'Dawn', 
    'Daylight', 
    'Dusk', 
    'Other', 
    'Unknown']
subgroups_dict['Junction Relationship'] = [
    'At Driveway', 
    'At Driveway within Major Intersection', 
    'At Intersection and Not Related', 
    'At Intersection and Related', 
    'At Roundabout but not Related', 
    'Circulating Roundabout', 
    'Driveway Related but Not at Driveway',
    'Entering Roundabout',
    'Exiting Roundabout',
    'Intersection Related but Not at Intersection',
    'Not at Intersection and Not Related',
    'Roundabout Related but not at Roundabout']
# subgroups_dict['TIME'] = [] could add something about night/day -- although also covered in lighting


def clean_dataframe():
    coords = pd.read_csv("data/coords_gps.csv")
    crashes = pd.read_csv("data/WA_Rural_St_RtesCrashes_Full.csv")
    # change the coordinates to be regular lat/lon
    crashes = crashes[crashes["WA STATE PLANE SOUTH - X 2010 - FORWARD"].notnull()].reset_index()
    crashes['Latitude'] = np.array(coords['Latitude'])
    crashes['Longitude'] = np.array(coords['Longitude'])
    # filter for general columns of interest
    crash_df = crashes.filter(["COUNTY", "DATE", "TIME", "MOST SEVERE INJURY TYPE", "WEATHER", "ROADWAY SURFACE CONDITION", "LIGHTING CONDITION", "JUNCTION RELATIONSHIP", "# INJ", "# FAT", "# VEH", "# PEDS", "# BIKES", "Latitude", "Longitude"])
    return crash_df
"""
Variables of the data that will be called from mapping.py to generate maps.
Functions for cleaning and merging the different data sources and dataframes.
"""
import warnings
import os
import pandas as pd
import numpy as np
warnings.filterwarnings('ignore')

MODULE_DIR = os.path.dirname(__file__)
MAPS_DIR = os.path.abspath(os.path.join(MODULE_DIR, '../outputs'))
DATA_DIR = MODULE_DIR + '../data/'


"""Common variables and functions that will be called by mapping.py"""

# all possible variables, {label in dataframe: label in GUI}
VARS_DICT = {}
VARS_DICT['Weather'] = 'WEATHER'
VARS_DICT['Surface Condition'] = 'ROADWAY SURFACE CONDITION'
VARS_DICT['Lighting Condition'] = 'LIGHTING CONDITION'
VARS_DICT['Junction Relationship'] = 'JUNCTION RELATIONSHIP'
#VARS_DICT['TIME'] = 'Time'

# reverse dict to above for writing output maps
GRP_DICT = {}
GRP_DICT['WEATHER'] = 'Weather'
GRP_DICT['ROADWAY SURFACE CONDITION'] = 'Surface_Condition'
GRP_DICT['LIGHTING CONDITION'] = 'Lighting_Condition'
GRP_DICT['JUNCTION RELATIONSHIP'] = 'Junction_Relationship'

INCIDENT_DICT = {}
INCIDENT_DICT['Injuries'] = '# INJ'
INCIDENT_DICT['Fatalities'] = '# FAT'
INCIDENT_DICT['Number of Vehicles Involved'] = '# VEH'

R_INCIDENT_DICT = {}
R_INCIDENT_DICT['# INJ'] = 'Injuries'
R_INCIDENT_DICT['# FAT'] = 'Fatalities'
R_INCIDENT_DICT['# VEH'] = 'Number of Vehicles Involved'

SUBGROUPS_DICT = {}
SUBGROUPS_DICT['Weather'] = [
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
SUBGROUPS_DICT['Surface Condition'] = [
    'Dry',
    'Ice',
    'Oil',
    'Other',
    'Sand/Mud/Dirt',
    'Snow/Slush',
    'Standing Water',
    'Unknown',
    'Wet']
SUBGROUPS_DICT['Lighting Condition'] = [
    'Dark-No Street Lights',
    'Dark-Street Lights Off',
    'Dark-Street Lights On',
    'Dawn',
    'Daylight',
    'Dusk',
    'Other',
    'Unknown']
SUBGROUPS_DICT['Junction Relationship'] = [
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
# SUBGROUPS_DICT['TIME'] = [] could add something about time


def clean_dataframe():
    """Cleaning the data used in in the app for pertinent information so it can
    be called on efficiently when generating the map based on user inputs at
    the interface."""

    coords = pd.read_csv(DATA_DIR + 'coords_gps.csv')
    crashes = pd.read_csv(DATA_DIR + 'WA_Rural_St_RtesCrashes_Full.csv')
    # change the coordinates to be regular lat/lon
    crashes = crashes[crashes["WA STATE PLANE SOUTH - X 2010 - FORWARD"].notnull()].reset_index()
    crashes['Latitude'] = np.array(coords['Latitude'])
    crashes['Longitude'] = np.array(coords['Longitude'])
    # filter for general columns of interest
    crash_df = crashes.filter(["COUNTY",
                               "DATE",
                               "TIME",
                               "MOST SEVERE INJURY TYPE",
                               "WEATHER",
                               "ROADWAY SURFACE CONDITION",
                               "LIGHTING CONDITION",
                               "JUNCTION RELATIONSHIP",
                               "# INJ", "# FAT", "# VEH",
                               "# PEDS", "# BIKES",
                               "Latitude", "Longitude"])
    years = []
    for date in crash_df['DATE']:
        years.append(date.split('/')[2])
    crash_df['Year'] = years
    return crash_df

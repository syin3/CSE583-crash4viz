"""
Variables of the data that will be called from mapping.py to generate maps.
Functions for cleaning and merging the different data sources and dataframes.
"""
import warnings
import os
import pandas as pd
import numpy as np
warnings.filterwarnings('ignore')

PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))
REPO_DIR = os.path.abspath(os.path.dirname(PACKAGE_DIR))
MAPS_DIR = os.path.abspath(os.path.join(REPO_DIR, 'outputs/'))
DATA_DIR = os.path.abspath(os.path.join(REPO_DIR, 'data/crash-merged/'))

"""Common variables and functions that will be called by mapping.py"""

# all possible variables, {label in dataframe: label in GUI}
VARS_DICT = {}
VARS_DICT['Weather'] = 'weather'
VARS_DICT['Surface Condition'] = 'RDSURF'
VARS_DICT['Lighting Condition'] = 'LIGHT'
# VARS_DICT['District Type'] = 'rur_urb' maybe not district type since they are already selecting county
VARS_DICT['Severity'] = 'SEVERITY'
VARS_DICT['Day of the week'] = 'WEEKDAY'
#VARS_DICT['TIME'] = 'Time'

COUNTY_DICT = {
    0: 'Not Stated',
    1:'Adams',
    2: 'Asotin',
    3: 'Benton',
    4: 'Chelan',
    5: 'Clallam',
    6: 'Clark',
    7:'Columbia',
    8: 'Cowlitz',
    9: 'Douglas', 
    10: 'Ferry',
    11: 'Franklin',
    12: 'Garfield',
    13: 'Grant',
    14: 'Grays Harbor',
    15: 'Island',
    16: 'Jefferson',
    17: 'King',
    18: 'Kitsap',
    19: 'Kittitas',
    20: 'Klickitat',
    21: 'Lewis',
    22: 'Lincoln',
    23: 'Mason',
    24: 'Okanogan',
    25: 'Pacific',
    26: 'Pend Oreille',
    27: 'Pierce',
    28: 'San Juan',
    29: 'Skagit',
    30: 'Skamania',
    31: 'Snohomish',
    32: 'Spokane',
    33: 'Stevens',
    34: 'Thurston',
    35: 'Wahkiakum',
    36: 'Walla Walla',
    37: 'Whatcom',
    38: 'Whitman',
    39: 'Yakima'}

R_COUNTY_DICT = {
    'Not Stated': 0,
    'Adams': 1,
    'Asotin': 2,
    'Benton': 3,
    'Chelan': 4,
    'Clallam': 5,
    'Clark': 6,
    'Columbia': 7,
    'Cowlitz': 8,
    'Douglas': 9, 
    'Ferry': 10,
    'Franklin': 11,
    'Garfield': 12,
    'Grant': 13,
    'Grays Harbor': 14,
    'Island': 15,
    'Jefferson': 16,
    'King': 17,
    'Kitsap': 18,
    'Kittitas': 19,
    'Klickitat': 20,
    'Lewis': 21,
    'Lincoln': 22,
    'Mason': 23,
    'Okanogan': 24,
    'Pacific': 25,
    'Pend Oreille': 26,
    'Pierce': 27,
    'San Juan': 28,
    'Skagit': 29,
    'Skamania': 30,
    'Snohomish': 31,
    'Spokane': 32,
    'Stevens': 33,
    'Thurston': 34,
    'Wahkiakum': 35,
    'Walla Walla': 36,
    'Whatcom': 37,
    'Whitman': 38,
    'Yakima': 39}


# reverse dict to above for writing output maps
GRP_DICT = {}
GRP_DICT['weather'] = 'Weather'
GRP_DICT['RDSURF'] = 'Surface_Condition'
GRP_DICT['LIGHT'] = 'Lighting_Condition'
GRP_DICT['rur_urb'] = 'District_type'
GRP_DICT['SEVERITY'] = 'Severity'
GRP_DICT['WEEKDAY'] = 'Day_of_week'

# dictionary for severity
INCIDENT_DICT = {1: 'Property Damage Only', 2: 'Injury Accident', 3: 'Fatal Accident'}

# reverse of above for writing maps
R_INCIDENT_DICT = {'Property Damage Only': 1, 'Injury Accident': 2, 'Fatal Accident': 3}

SUBGROUPS_DICT = {}
SUBGROUPS_DICT['Weather'] = {
    0: 'Unknown',
    1: 'Clear or Partly Cloudy',
    2: 'Overcast',
    3: 'Raining',
    4: 'Snowing',
    5: 'Fog/Smog/Smoke',
    6: 'Sleet/Hail/Freezing Rain',
    7: 'Severe Crosswind',
    8: 'Blowing Sand or Dirt or Snow',
    9: 'Other',
    10: 'Foggy'}
SUBGROUPS_DICT['Surface Condition'] = {
    1.0: 'Dry',
    2.0: 'Wet',
    3.0: 'Snow/Slush',
    4.0: 'Ice',
    5.0: 'Sand/Mud/Dirt',
    6.0: 'Oil',
    7.0: 'Standing Water',
    8.0: 'Other',
    9.0: 'Unknown',
    np.nan: 'Unknown'}
SUBGROUPS_DICT['Lighting Condition'] = {
    1.0: 'Daylight',
    2.0: 'Dawn',
    3.0: 'Dusk',
    4.0: 'Dark, Street Lights On',
    5.0: 'Dark, Street Lights Off',
    6.0: 'No Street Lights',
    7.0: 'Other',
    9.0: 'Unknown',
    np.nan: 'Unknown'}
SUBGROUPS_DICT['Day of the week'] = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'}

R_SUBGROUPS_DICT = {}
R_SUBGROUPS_DICT['Weather'] = {
    'Unknown': 0,
    'Clear or Partly Cloudy': 1,
    'Overcast': 2,
    'Raining': 3,
    'Snowing': 4,
    'Fog/Smog/Smoke': 5,
    'Sleet/Hail/Freezing Rain': 6,
    'Severe Crosswind': 7,
    'Blowing Sand or Dirt or Snow': 8,
    'Other': 9,
    'Foggy': 10}
R_SUBGROUPS_DICT['Surface Condition'] = {
    'Dry': 1.0,
    'Wet': 2.0,
    'Snow/Slush': 3.0,
    'Ice': 4.0,
    'Sand/Mud/Dirt': 5.0,
    'Oil': 6.0,
    'Standing Water': 7.0,
    'Other': 8.0,
    'Unknown': 9.0,
    'Unknown': np.nan}
R_SUBGROUPS_DICT['Lighting Condition'] = {
    'Daylight': 1.0,
    'Dawn': 2.0,
    'Dusk': 3.0,
    'Dark, Street Lights On': 4.0,
    'Dark, Street Lights Off': 5.0,
    'No Street Lights': 6.0,
    'Other': 7.0,
    'Unknown': 9.0,
    'Unknown': np.nan}
R_SUBGROUPS_DICT['Day of the week'] = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7}


def read_dataframe(year):
    """
    read a dataset by year
    """
    data = pd.read_csv(DATA_DIR + '/{}.csv'.format(year))
    return data

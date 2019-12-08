#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
merge.py
reads in NOAA converted coordinates and merge with accident, road, grade, curve files
'''


# ### import

# In[1]:


import os
import pandas as pd
import sqlite3


# ### function

# #### read noaa coords

# In[2]:


def read_noaa_coords(yr, directory):
    columns = ['ID', 'destLat', 'destLon']
    
    # detect all csv files of the year
    yr_file_list = []
    for file in os.listdir(directory):
        if str(yr) in file:
            yr_file_list.append(file)
    
    # sort so that No.0 file is at the first place
    yr_file_list = sorted(yr_file_list)
    
    # read and append the dataframes
    count = 0
    for file in yr_file_list:
        if count == 0:
            records = pd.read_csv(directory + '/' + file)
            records = records[columns]
        else:
            records = records.append(pd.read_csv(directory + '/' + file)[columns]).reset_index(drop=True)
        
        count += 1
    
    records.columns = ['ID', 'lat', 'lon']
    return records


# #### detect files with keywords in name

# In[3]:


def detect_files(directory, keyword):
    file_list = []
    for file in os.listdir(directory):
        if keyword in file:
            file_list.append(file)
    
    return sorted(file_list)


# #### merge noaa coords with acc and clean

# In[4]:


def acc_merge(acc_file_list, noaa_coords, directory):
    crashes = {}
    for file in acc_file_list:
        yr = file[2:4]
        acc_file = directory + '/' + file
        tmp = pd.read_csv(acc_file)
        tmp = tmp.dropna(subset=['State_Plane_X', 'State_Plane_Y'])
        tmp['ID'] = tmp.index + 1
        crashes[2000+int(yr)] = tmp
    
    for yr in noaa_coords.keys():
        crashes[yr] = crashes[yr].merge(noaa_coords[yr], on='ID', how='inner')
    
    columns = ['CASENO', 'FORM_REPT_NO', 'rd_inv', 'milepost', 'RTE_NBR',
           'lat', 'lon', 
           'MONTH', 'DAYMTH', 'WEEKDAY', 
           'RDSURF', 'LIGHT', 'weather', 'rur_urb',
           'REPORT', 'SEVERITY']

    for yr in crashes.keys():
        crashes[yr] = crashes[yr][columns]
    
    return crashes


# #### read files with keyword and directory

# In[5]:


def read_files(directory, keyword):
    output_dic = {}
    file_list = detect_files(directory, keyword)
    for yr in range(2013, 2018):
        output_dic[yr] = pd.read_csv(directory + '/' + file_list[yr-2013])
    return output_dic


# #### final meta merge func

# In[6]:


def meta_merge(crashes, curv, grad, occ, road, veh):
    """
    they have the same keys (of year 2013 to 2017)
    """
    meta = {}
    for yr in range(2013, 2018):
        # first merge veh count with crashes
        veh_count = veh[yr]['CASENO'].value_counts().sort_index()
        veh_count = veh_count.to_frame().reset_index()
        veh_count.columns = ['CASENO', 'veh_count']
        
        acc_this_yr = crashes[yr].merge(veh_count, on='CASENO', how='inner')
        
        # road
        road_this_yr = road[yr].drop(['RTE_NBR'], axis=1)
        conn = sqlite3.connect(":memory:")
        acc_this_yr.to_sql("crash", conn, index=False)
        road_this_yr.to_sql("road", conn, index=False)
        query =             "SELECT *             FROM crash, road            WHERE crash.rd_inv = road.ROAD_INV            AND crash.milepost >= road.BEGMP            AND crash.milepost <= road.ENDMP"
        records = pd.read_sql_query(query, conn)
        
        ## remove duplicates randomly
        records = records.sample(frac=1).drop_duplicates(subset='CASENO').sort_index()
        
        # curve
        curv_this_yr = curv[yr]
        conn = sqlite3.connect(":memory:")
        records.to_sql("records", conn, index=False)
        curv_this_yr.to_sql("curv", conn, index=False)
        
        query =             "SELECT *             FROM records LEFT JOIN curv ON records.rd_inv = curv.curv_inv            AND records.milepost >= curv.begmp            AND records.milepost <= curv.endmp"
        records = pd.read_sql_query(query, conn)
        
        ## remove duplicates and drop useless attributes
        records = records.sample(frac=1).drop_duplicates(subset='CASENO').sort_index()
        records = records.drop(['curv_inv', 'begmp', 'endmp', 'rte_nbr', 'DIR_CURV'], axis=1)
        
        ## fill NaN curvature with 0
        records = records.fillna(value={'deg_curv': 0})
        
        # grad
        grad_this_yr = grad[yr]
        conn = sqlite3.connect(":memory:")
        records.to_sql("records", conn, index=False)
        grad_this_yr.to_sql("grad", conn, index=False)
        
        query =             "SELECT *             FROM records LEFT JOIN grad ON records.rd_inv = grad.grad_inv            AND records.milepost >= grad.begmp            AND records.milepost <= grad.endmp"
        
        records = pd.read_sql_query(query, conn)
        
        records = records.drop(['grad_inv', 'begmp', 'endmp', 'rte_nbr'], axis=1)
        records = records.sample(frac=1).drop_duplicates(subset='CASENO').sort_index()
        
        records = records.fillna(value={'pct_grad': 0})
    
        # when everything is done, save
        meta[yr] = records
    return meta


# ### read NOAA converted coordinates

# In[7]:


noaa_coords = {}
for yr in range(2013, 2018):
    noaa_coords[yr] = read_noaa_coords(yr, '../../data/coords-noaa')


# ### merge NOAA coodinates to acc records

# #### detect and read all acc files

# In[8]:


acc_file_list = detect_files("../../data/hsis-csv", 'acc')
crashes = acc_merge(acc_file_list, noaa_coords, '../../data/hsis-csv')


# ### Merge with other files

# #### read them first

# In[9]:


curv = read_files("../../data/hsis-csv", 'curv')
grad = read_files("../../data/hsis-csv", 'grad')
occ = read_files("../../data/hsis-csv", 'occ')
road = read_files("../../data/hsis-csv", 'road')
veh = read_files("../../data/hsis-csv", 'veh')


# #### meta merge

# In[10]:


met = meta_merge(crashes, curv, grad, occ, road, veh)
for yr in range(2013, 2018):
    met[yr].to_csv('../../data/crash-merged/{}.csv'.format(yr), index=False)


# In[ ]:





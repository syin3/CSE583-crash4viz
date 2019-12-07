#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
coords_conversion.py
reads in CSV files, prepares dataset for NOAA website multi-point conversion
'''


# In[1]:


import os
import pandas as pd


# ### detect acc csv file

# In[2]:


directory = "./data/hsis-csv"

acc_file_list = []
for file in os.listdir(directory):
    if 'acc' in file:
        acc_file_list.append(file)


# ### read csv and prepare

# In[8]:


for file in acc_file_list:
    yr = file[2:4]
    acc_file = directory + '/' + file
    acc = pd.read_csv(acc_file)
    
    columns = ['FORM_REPT_NO', 'State_Plane_X', 'State_Plane_Y']
    acc = acc[columns]
    acc.columns = ['REPORT NUMBER', 'X_full', 'Y_full']
    
    acc = acc.dropna(subset=['X_full', 'Y_full']).reset_index()
    
    output = acc[['Y_full', 'X_full']]
    output.columns = ['northing', 'easting']
    output['zone'] = 4602
    output['units'] = 'usft'
    output['inDatum'] = 'NAD83(2011)'
    output['outDatum'] = 'NAD83(2011)'
    output['utmZone'] = 'auto'
    output['eht'] = 'N/A'
    output['ID'] = output.index + 1
    
    output = output[['ID', 'zone', 'northing', 'easting', 'units', 'inDatum', 'outDatum', 'utmZone', 'eht']]
    
    for i in range(output.shape[0] // 4000):
        output[(i*4000):((i+1)*4000)].to_csv('./data/coords2convert/acc_{}_{}.csv'.format(yr, i), index=None, sep=',')
    output[((i+1)*4000):].to_csv('./data/coords2convert/acc_{}_{}.csv'.format(yr, i+1), index=None, sep=',')


# In[ ]:





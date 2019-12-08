#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
create-sample.py
create sample test data
'''


# In[1]:


import os
import pandas as pd


# ### load, sample and save

# In[2]:


columns = ['CASENO','FORM_REPT_NO','rd_inv','milepost','RTE_NBR','lat','lon','MONTH','DAYMTH','WEEKDAY','RDSURF','LIGHT',
 'weather','rur_urb','REPORT','SEVERITY','veh_count','LSHL_TYP','MED_TYPE','RD_LIGHT','RSHL_TYP','RURURB','SURF_TYP','EW_IND',
 'COUNTY','FUNC_CLS','CITY','ROAD_INV','SPD_LIMT','BEGMP','ENDMP','ACSEQ_NB','LSHLDWID','MEDWID','NO_LANES','RSHLDWID','lanewid',
 'rdwy_wid','AADT','mvmt','deg_curv','dir_grad','pct_grad']
df = pd.DataFrame(columns=columns)


# In[3]:


mydir = '../../data/crash-merged/'
for file in os.listdir(mydir):
    if file.endswith(".csv"):
        tmp = pd.read_csv(mydir + file)
        tmp = tmp.sample(n = 500, random_state=0)
        df = df.append(tmp).reset_index(drop=True)


# In[4]:


df.to_csv('../tests/test-data/sample.csv', index=False)


# In[ ]:





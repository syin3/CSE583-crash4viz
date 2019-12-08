#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
xslx2csv.py
Converts datasets in xslx format to csv in the given directory
'''


# In[7]:


import os
import pandas as pd


# In[8]:


file_list = []
for file in os.listdir("../../data/hsis"):
    if file.endswith(".xlsx"):
        file_list.append(file)
print('Found {} target file(s) in the current folder...\n'.format(len(file_list)))

file_list = sorted(file_list, reverse=True)


# In[15]:


attributes = {}
for file in file_list:
    curr = pd.read_excel('../../data/hsis/' + file)
    if '17' in file:
        attributes[file.split('.')[0][4:]] = list(curr.columns)
    curr.columns = attributes[file.split('.')[0][4:]]
    curr.to_csv('../../data/hsis-csv/' + file.split('.')[0] + '.csv', index=False)
    print('Finished file: {}'.format(file))


# In[ ]:





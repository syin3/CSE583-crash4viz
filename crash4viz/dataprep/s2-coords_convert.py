#!/usr/bin/env python
# coding: utf-8

'''
coords_conversion.py
reads in CSV files, prepares dataset for NOAA website multi-point conversion
'''

import os
import pandas as pd

def save4noaa(ori_direct, save4noaa_direct):
    '''
    split original state plane coordinates to 4000 records per file
    to prepare for NOAA's coordinate conversion
    @param ori_direct: directory where the original accident files are
    @param save4noaa_direct: directory where split coord csv files go
    @test:
        (1) if the directories exist;
        (2) if acc file list is not empty;
        (3) if output files in NOAA directory have in total equal number of lines
    '''

    acc_file_list = []
    for file in os.listdir(ori_direct):
        if 'acc' in file:
            acc_file_list.append(file)

    for file in acc_file_list:
        yr = file[2:4]
        acc_file = ori_direct + '/' + file
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
            output[(i*4000):((i+1)*4000)].to_csv(save4noaa_direct + '/acc_{}_{}.csv'.format(yr, i), index=None, sep=',')
        output[((i+1)*4000):].to_csv(save4noaa_direct + '/acc_{}_{}.csv'.format(yr, i+1), index=None, sep=',')

    pass

# save4noaa('../../data/hsis-csv', '../../data/coords2convert')
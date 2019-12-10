#!/usr/bin/env python
# coding: utf-8

'''
merge.py
reads in NOAA converted coordinates and merge with accident, road, grade, curve files
'''

import os
import pandas as pd
import sqlite3

def read_noaa_coords(yr, directory):
    '''
    read from NOAA converted coords
    @param yr: year to combine
    @param directory: where to read NOAA converted files from
    @output records: combined coords for the specified year
    @test
        (1) if number of files is greater than zero
        (2) if records has non-zero length
        (3) if records' num of columns is three
    '''
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

def detect_files(directory, keyword):
    '''
    detect files in specified directory with specified keyword
    @param directory: dir to search
    @param keyword: keyword to look for
    @output sorted list of file names
    @test:
        (1) if output has larger than length
    '''
    file_list = []
    for file in os.listdir(directory):
        if keyword in file:
            file_list.append(file)
    
    return sorted(file_list)

def acc_merge(acc_file_list, noaa_coords, directory):
    '''
    merge accidents with NOAA coords
    @param acc_file_list: sorted list of accident file names
    @param noaa_coords: combined NOAA records
    @param directory: directory of accident files
    @output crashes: dictionary of merged crahses
    @test:
        (1) crash dictionary should have 5 key-values, 2013-2017
        (2) 16 columns in merged datasets
        (3) weather and light should be in float, but may have NaN
        (4) crash should not be empty
    '''
    # create dictionary of crashes, key is year
    crashes = {}
    for file in acc_file_list:
        yr = file[2:4]
        acc_file = directory + '/' + file
        tmp = pd.read_csv(acc_file)
        tmp = tmp.dropna(subset=['State_Plane_X', 'State_Plane_Y']).reset_index()
        tmp['ID'] = tmp.index + 1
        crashes[2000+int(yr)] = tmp
    
    # merge noaa records with corresponding year of accidents
    for yr in noaa_coords.keys():
        crashes[yr] = crashes[yr].merge(noaa_coords[yr], on='ID', how='inner')
    
    # specify columns to keep
    columns = ['CASENO', 'FORM_REPT_NO', 'rd_inv', 'milepost', 'RTE_NBR',
           'lat', 'lon', 
           'MONTH', 'DAYMTH', 'WEEKDAY', 
           'RDSURF', 'LIGHT', 'weather', 'rur_urb',
           'REPORT', 'SEVERITY']

    # convert string of light and weather to float, but keep NaN
    for yr in crashes.keys():
        crashes[yr] = crashes[yr][columns]
        crashes[yr].LIGHT = pd.to_numeric(crashes[yr].LIGHT, errors='coerce')
        crashes[yr].weather = pd.to_numeric(crashes[yr].weather, errors='coerce')
    
    return crashes

def read_files(directory, keyword):
    '''
    read files with specified keyword
    @param directory: directory to read files from
    @param keyword: keyword to search for
    @output output_dic: dictionary of datasets
    @test:
        (1) output_dic should have length 5
        (2) keyword should not be empty
    '''
    output_dic = {}
    file_list = detect_files(directory, keyword)
    for yr in range(2013, 2018):
        output_dic[yr] = pd.read_csv(directory + '/' + file_list[yr-2013])
    return output_dic

def meta_merge(crashes, curv, grad, occ, road, veh):
    '''
    they have the same keys (of year 2013 to 2017)
    merge various sources to final accident files
    @param crashes: crashes with noaa coords
    @param curv: curv dictionary with 5 years of data
    @param grad: grade dictionary with 5 years of data
    @param occ: occupant dictionary with 5 years of data
    @param raod: road dictionary with 5 years of data
    @param veh: vehicle dictionary with 5 years of data
    @output meta: dictionary of 5 years of merged meta dataset
    @test:
        (1) every input has length 5
        (2) crashes, occ, veh have key 'CASENO'
        (3) 22 columns in output datasets
        (4) output has length 5
        (5) no nan in final output datasets
        (6) -2 column are all string type
    '''
    meta = {}
    for yr in range(2013, 2013 + len(crashes)):
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
        query =  "SELECT * FROM crash, road \
        WHERE crash.rd_inv = road.ROAD_INV\
        AND crash.milepost >= road.BEGMP\
        AND crash.milepost <= road.ENDMP"
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
        
        query = "SELECT * FROM records \
        LEFT JOIN grad ON records.rd_inv = grad.grad_inv\
        AND records.milepost >= grad.begmp\
        AND records.milepost <= grad.endmp"
        
        records = pd.read_sql_query(query, conn)
        
        records = records.drop(['grad_inv', 'begmp', 'endmp', 'rte_nbr'], axis=1)
        records = records.sample(frac=1).drop_duplicates(subset='CASENO').sort_index()
        
        records = records.fillna(value={'pct_grad': 0})
        
        columns = ['CASENO', 'FORM_REPT_NO', 'rd_inv', 'milepost', 'RTE_NBR', 'lat', 'lon',
                   'MONTH', 'DAYMTH', 'WEEKDAY', 'RDSURF', 'LIGHT', 'weather', 'rur_urb',
                   'REPORT', 'veh_count', 'COUNTY', 'AADT', 'mvmt', 'deg_curv', 'dir_grad',
                   'pct_grad']
        records = records[columns]
        
        for i in range(records.shape[0]):
            if not isinstance(records.iloc[i, -2], str):
                records.iloc[i, -2] = '0'
    
        records = records.dropna()
        # when everything is done, save
        meta[yr] = records
    return meta

# noaa_coords = {}
# for yr in range(2013, 2018):
#     noaa_coords[yr] = read_noaa_coords(yr, '../../data/coords-noaa')

# acc_file_list = detect_files("../../data/hsis-csv", 'acc')
# crashes = acc_merge(acc_file_list, noaa_coords, '../../data/hsis-csv')

# curv = read_files("../../data/hsis-csv", 'curv')
# grad = read_files("../../data/hsis-csv", 'grad')
# occ = read_files("../../data/hsis-csv", 'occ')
# road = read_files("../../data/hsis-csv", 'road')
# veh = read_files("../../data/hsis-csv", 'veh')

# met = meta_merge(crashes, curv, grad, occ, road, veh)
# for yr in range(2013, 2018):
#     met[yr].to_csv('../../data/crash-merged/{}.csv'.format(yr), index=False)
#     print('finished {}'.format(yr))


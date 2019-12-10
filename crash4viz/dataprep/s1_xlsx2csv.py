#!/usr/bin/env python
# coding: utf-8

'''
xslx2csv.py
Converts datasets in xslx format to csv in the given directory
'''

import os
import pandas as pd

def find_excel(direct):
    '''
    Finds all excel files in a given directory
    @param direct: directory to read all excelf files from
    @output files_list: sorted list of names of detected files of target type
    @test:
        (1) test if file_list is sorted;
        (2) test if all xlsx files are in the list
    '''
    file_list = []
    # iterate through designated directory
    for file in os.listdir(direct):
        if file.endswith(".xlsx"):
            file_list.append(file)

    # sort the file list in reverse order
    file_list = sorted(file_list, reverse=True)
    return file_list

def convert_xlsx2csv(xlsx_direct, csv_direct, file_list):
    '''
    Converts excel files in the list to csv files
    @param xlsx_direct: directory of excel files
    @param csv_direct: directory of csv files
    @param file_list: list of excel files to be converted
    @test: 
        (1) test if column names are the same for the same file over years;
        (2) test if all excel files have one and only one csv
    '''
    attributes = {}
    for file in file_list:
        curr = pd.read_excel(xlsx_direct + file)
        # remember column names from 2017 file
        # and rename columns from other years in 2017 style
        if '17' in file:
            attributes[file.split('.')[0][4:]] = list(curr.columns)
        curr.columns = attributes[file.split('.')[0][4:]]

        # save as corresponding csv files in output directory
        curr.to_csv(csv_direct + file.split('.')[0] + '.csv', index=False)

    # return nothing
    pass

# file_list = find_excel("../../data/hsis")
# convert_xlsx2csv('../../data/hsis/', '../../data/hsis-csv/', file_list)

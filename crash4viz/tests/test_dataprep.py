"""
Unit tests for ensuring data preps are corect.
Run these tests from the top-most directory of the WAcrashviz package.
"""

import unittest
import os
import inspect
import sys
import warnings

# tests
CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# crash4viz/crash4viz
PARENTDIR = os.path.dirname(CURRENTDIR)
# crash4viz
PARENT = os.path.dirname(PARENTDIR)
sys.path.insert(0, PARENT)

from crash4viz.dataprep import milepost
from crash4viz.dataprep import s1_xlsx2csv
from crash4viz.dataprep import s2_coords_convert
from crash4viz.dataprep import s3_merge

TEST_OUTPUT = CURRENTDIR + '/test_output/'

class TestDataPrep(unittest.TestCase):
    '''
    Test the data prep scripts in crash4viz/data prep folder.
    '''

    def setUp(self):
        warnings.simplefilter('ignore')

    def test_read_milepost(self):
        """Test that the features being drawn from dictionaries that the
        mapping function will call on for plotting are correct."""
        
        mileposts = milepost.read_milepost(PARENT + '/data/milepost/SRMilepostMarkers.shp')
        self.assertNotEqual(len(mileposts[0]), 0,
                         "Milepost function didn't read any latitude")
        self.assertNotEqual(len(mileposts[1]), 0,
                         "Milepost function didn't read any longitude")

    def test_plot_milepost(self):
        """Test if milepost is plotted correctly"""
        mileposts = milepost.read_milepost(PARENT + '/data/milepost/SRMilepostMarkers.shp')
        _ = milepost.plot_milepost(mileposts, TEST_OUTPUT + 'test_milepost.html')
        self.assertEqual(
            (os.path.isfile(TEST_OUTPUT + 'test_milepost.html')),
            True,
            "Milepost did not output correctly")

    def test_find_excel(self):
        """Test if excel files can be found successfully"""
        file_list = s1_xlsx2csv.find_excel(PARENT + '/data/hsis')
        self.assertEqual(len(file_list), 30, "Find excel is not counting right")

    def test_convert_xlsx2csv(self):
        """Test if excel files can be found successfully"""
        file_list = s1_xlsx2csv.find_excel(PARENT + '/data/hsis/')
        s1_xlsx2csv.convert_xlsx2csv(PARENT + '/data/hsis/', PARENT + '/data/hsis-csv/', file_list)
        csv_list = []
        for file in os.listdir(PARENT + '/data/hsis-csv/'):
            if file.endswith(".csv"):
                csv_list.append(file)
        self.assertEqual(len(csv_list), 30, "CSV conversion is not correct")

    def test_save4noaa(self):
        """Test if savign for NOAA conversion is successful"""
        s2_coords_convert.save4noaa(PARENT + '/data/hsis-csv/', PARENT + '/data/coords2convert/')
        csv_list = []
        for file in os.listdir(PARENT + '/data/coords2convert/'):
            if file.endswith(".csv") and 'acc' in file:
                csv_list.append(file)
        self.assertEqual(len(csv_list), 67, "CSV conversion is not correct")

    def test_read_noaa_coords(self):
        """Test reading NOAA converted coords"""
        for yr in range(2013, 2018):
            records = s3_merge.read_noaa_coords(yr, PARENT + '/data/coords-noaa/')
            self.assertEqual(records.shape[1], 3, "Reading NOAA converted coords is incorrect.")

    def test_acc_merge(self):
        """Test acc merge with NOAA coords"""
        noaa_coords = {}
        for yr in range(2013, 2018):
            noaa_coords[yr] = s3_merge.read_noaa_coords(yr, PARENT + '/data/coords-noaa/')
        acc_file_list = s3_merge.detect_files(PARENT + "/data/hsis-csv", 'acc')
        crashes = s3_merge.acc_merge(acc_file_list, noaa_coords, PARENT + '/data/hsis-csv')

        self.assertEqual(len(crashes), 5, "accident merging with NOAA coords is wrong.")
        for each in crashes:
            self.assertEqual(each.shape[1], 16, "Merged accident files subsetting is wrong.")

    def test_meta_merge(self):
        """Test meta merge"""
        noaa_coords = {}
        for yr in range(2013, 2018):
            noaa_coords[yr] = s3_merge.read_noaa_coords(yr, PARENT + '/data/coords-noaa')

        acc_file_list = s3_merge.detect_files(PARENT + "/data/hsis-csv", 'acc')
        crashes = s3_merge.acc_merge(acc_file_list, noaa_coords, PARENT + '/data/hsis-csv')

        curv = s3_merge.read_files(PARENT + "/data/hsis-csv", 'curv')
        grad = s3_merge.read_files(PARENT + "/data/hsis-csv", 'grad')
        occ = s3_merge.read_files(PARENT + "/data/hsis-csv", 'occ')
        road = s3_merge.read_files(PARENT + "/data/hsis-csv", 'road')
        veh = s3_merge.read_files(PARENT + "/data/hsis-csv", 'veh')

        for key in crashes.keys():
            self.assertEqual('CASENO' in list(crashes[key].columns), True, 'supporting doc reading problematic')
            self.assertEqual('CASENO' in list(occ[key].columns), True, 'supporting doc reading problematic.')
            self.assertEqual('CASENO' in list(veh[key].columns), True, 'supporting doc reading problematic..')

        meta = s3_merge.meta_merge(crashes, curv, grad, occ, road, veh)
        self.assertEqual(len(meta), 5, "meta merge wrong.")

        for key in meta.keys():
            self.assertEqual(meta[key].shape[1], 22, "Meta merging problem.")
            self.assertEqual(meta[key].isna().sum().sum(), 0, "Meta merging did not drop na.")

if __name__ == '__main__':
    unittest.main()

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
from crash4viz.dataprep import s4_folium_prep

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
        
        milepost = milepost.read_milepost(PARENT + '/data/milepost/SRMilepostMarkers.shp')
        self.assertNotEqual(len(milepost[0]), 0,
                         "Milepost function didn't read any latitude")
        self.assertNotEqual(len(milepost[1]), 0,
                         "Milepost function didn't read any longitude")

    def test_plot_milepost(self):
        """Test if milepost is plotted correctly"""
        mileposts = milepost.read_milepost(PARENT + '/data/milepost/SRMilepostMarkers.shp')
        _ = milepost.plot_milepost(mileposts, TEST_OUTPUT + 'test_milepost.html')
        self.assertEqual(
            (os.path.isfile(TEST_OUTPUT + 'test_milepost.html')),
            True,
            "Milepost did not output correctly")

if __name__ == '__main__':
    unittest.main()

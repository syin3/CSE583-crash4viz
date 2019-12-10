"""Tests for ML predictions script outputs and functions."""

import os
import unittest
import pandas as pd
import inspect
import sys
import tkinter
CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENTDIR = os.path.dirname(CURRENTDIR)
PARENT = os.path.dirname(PARENTDIR)
sys.path.insert(0, PARENT)
from crash4viz import mapping_funcs
from crash4viz import mlpredict
import warnings

TEST_OUTPUT = CURRENTDIR + '/test_output/'

class TestMappingFuncs(unittest.TestCase):
    """Tests to ensure that basic components of the framework is being
    loaded correctly and paths are pointed to the right places."""

    def setUp(self):
        """Disable pandas dtype warnings."""

        warnings.simplefilter('ignore')

    def test_mlpredict(self):
        """Test that the different functions being called in mlpredict.py produce
        the plots it's supposed to in the location that it's supposed to."""

        year_plot_list = []
        for yr in range(2013, 2018):
            year_plot_list.append(pd.read_csv(mapping_funcs.DATA_DIR + '/{}.csv'.format(yr)).shape[0])
        _ = mlpredict.year_plot(year_plot_list, TEST_OUTPUT)

        df_2017 = pd.read_csv(mapping_funcs.DATA_DIR + "/2017.csv")

        _ = mlpredict.month_plot(df_2017, TEST_OUTPUT)
        _ = mlpredict.weekday_plot(df_2017, TEST_OUTPUT)
        _ = mlpredict.weather_plot(df_2017, TEST_OUTPUT)
        _ = mlpredict.road_plot(df_2017, TEST_OUTPUT)
        _ = mlpredict.light_plot(df_2017, TEST_OUTPUT)
        _ = mlpredict.ml_prediction(df_2017, TEST_OUTPUT)
        self.assertEqual((os.path.isfile(TEST_OUTPUT + '/year_plot.png') and
                              os.path.isfile(TEST_OUTPUT + '/month_plot.png') and
                              os.path.isfile(TEST_OUTPUT + 'weekday_plot.png') and
                              os.path.isfile(TEST_OUTPUT + 'weather_plot.png') and
                              os.path.isfile(TEST_OUTPUT + 'road_plot.png') and
                              os.path.isfile(TEST_OUTPUT + 'light_plot.png') and
                              os.path.isfile(TEST_OUTPUT + 'weather_factor_importance.png')),
                             True,
                             "Missing one or more outputs")

    def test_months(self):
        """Test that the month_plot function is accessing the correct data."""

        test_df = pd.read_csv(mapping_funcs.DATA_DIR + "/2017.csv")
        test_out = mlpredict.month_plot(test_df, TEST_OUTPUT)
        self.assertEqual(len(test_out), 12,
                         "The dataframe counts for month are incorrect.")

    def test_weekday(self):
        """Test that the weekday_plot function is accessing the correct data."""

        test_df = pd.read_csv(mapping_funcs.DATA_DIR + "/2017.csv")
        test_out = mlpredict.weekday_plot(test_df, TEST_OUTPUT)
        self.assertEqual(len(test_out), 7,
                         "The dataframe counts for weekday are incorrect.")

    def test_weather(self):
        """Test that the weather_plot function is accessing the correct data."""
        
        test_df = pd.read_csv(mapping_funcs.DATA_DIR + "/2017.csv")
        test_out = mlpredict.weather_plot(test_df, TEST_OUTPUT)
        self.assertEqual(len(test_out), 10,
                         "The dataframe counts for weather are incorrect.")

    def test_road(self):
        """Test that the road_plot function is accessing the correct data."""

        test_df = pd.read_csv(mapping_funcs.DATA_DIR + "/2017.csv")
        test_out = mlpredict.road_plot(test_df, TEST_OUTPUT)
        self.assertEqual(len(test_out), 9,
                         "The dataframe counts for road surface are incorrect.")

    def test_light(self):
        """Test that the light_plot function is accessing the correct data."""

        test_df = pd.read_csv(mapping_funcs.DATA_DIR + "/2017.csv")
        test_out = mlpredict.light_plot(test_df, TEST_OUTPUT)
        self.assertEqual(len(test_out), 8,
                         "The dataframe counts for light are incorrect.")

    def test_mlprediction(self):
        """Test that the light_plot function is accessing the correct data."""

        test_df = pd.read_csv(mapping_funcs.DATA_DIR + "/2017.csv")
        test_out = mlpredict.ml_prediction(test_df, TEST_OUTPUT)
        self.assertEqual(len(test_out), 5,
                         "Wrong number of features for which importance is calculated.")

if __name__ == '__main__':
    unittest.main()

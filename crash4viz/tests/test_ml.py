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

TEST_OUTPUT = CURRENTDIR + '/test_output/'

merged_data_2013 = pd.read_csv(mapping_funcs.DATA_DIR + '/2013.csv')
merged_data_2014 = pd.read_csv(mapping_funcs.DATA_DIR + '/2014.csv')
merged_data_2015 = pd.read_csv(mapping_funcs.DATA_DIR + '/2015.csv')
merged_data_2016 = pd.read_csv(mapping_funcs.DATA_DIR + '/2016.csv')
merged_data_2017 = pd.read_csv(mapping_funcs.DATA_DIR + '/2017.csv')
df_2017 = pd.read_csv(mapping_funcs.DATA_DIR + "/2017.csv")

def test_mlpredict():
    mlpredict.year_plot(merged_data_2013, merged_data_2014,
                        merged_data_2015, merged_data_2016,
                        merged_data_2017, TEST_OUTPUT)
    mlpredict.month_plot(df_2017, TEST_OUTPUT)
    mlpredict.weekday_plot(df_2017, TEST_OUTPUT)
    mlpredict.weather_plot(df_2017, TEST_OUTPUT)
    mlpredict.road_plot(df_2017, TEST_OUTPUT)
    mlpredict.light_plot(df_2017, TEST_OUTPUT)
    mlpredict.ml_prediction(df_2017, TEST_OUTPUT)
    unittest.assertEqual((os.path.isfile(TEST_OUTPUT + '/year_plot.png') and
                          os.path.isfile(TEST_OUTPUT + '/month_plot.png') and
                          os.path.isfile(TEST_OUTPUT + 'weekday_plot.png') and
                          os.path.isfile(TEST_OUTPUT + 'weather_plot.png') and
                          os.path.isfile(TEST_OUTPUT + 'road_plot.png') and
                          os.path.isfile(TEST_OUTPUT + 'light_plot.png') and
                          os.path.isfile(TEST_OUTPUT + 'weather_factor_importance.png')),
                         True,
                         "Missing one or more outputs")


if __name__ == '__main__':
    unittest.main()

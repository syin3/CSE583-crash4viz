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

def test_mlpredict():
    year_plot_list = []
    for yr in range(2013, 2018):
        year_plot_list.append(pd.read_csv(mapping_funcs.DATA_DIR + '/2013.csv').shape[0])
    mlpredict.year_plot(year_plot_list, TEST_OUTPUT)

    df_2017 = pd.read_csv(mapping_funcs.DATA_DIR + "/2017.csv")
    
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

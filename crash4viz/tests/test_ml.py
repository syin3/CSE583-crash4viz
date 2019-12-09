import os
import unittest
import pandas as pd
import crash4viz.mlpredict as mlpredict

merged_data_2013 = pd.read_csv('../../data/crash-merged/2013.csv')
merged_data_2014 = pd.read_csv('../../data/crash-merged/2014.csv')
merged_data_2015 = pd.read_csv('../../data/crash-merged/2015.csv')
merged_data_2016 = pd.read_csv('../../data/crash-merged/2016.csv')
merged_data_2017 = pd.read_csv('../../data/crash-merged/2017.csv')
df_2017 = pd.read_csv("../../data/crash-merged/2017.csv")


def test_mlpredict():
    mlpredict.year_plot(merged_data_2013, merged_data_2014,
                        merged_data_2015, merged_data_2016, merged_data_2017)
    mlpredict.month_plot(df_2017)
    mlpredict.weekday_plot(df_2017)
    mlpredict.weather_plot(df_2017)
    mlpredict.road_plot(df_2017)
    mlpredict.light_plot(df_2017)
    mlpredict.ml_prediction(df_2017)
    unittest.assertEqual((os.path.isfile('../../outputs/year_plot.png') and
                          os.path.isfile('../../outputs/month_plot.png') and
                          os.path.isfile('../../outputs/weekday_plot.png') and
                          os.path.isfile('../../outputs/weather_plot.png') and
                          os.path.isfile('../../outputs/road_plot.png') and
                          os.path.isfile('../../outputs/light_plot.png') and
                          os.path.isfile('../../outputs/weather_factor_importance.png')),
                         True,
                         "Missing one or more outputs")


if __name__ == '__main__':
    unittest.main()

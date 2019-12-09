# Crash4viz
[![Coverage Status](https://coveralls.io/repos/github/syin3/crash4viz/badge.svg?branch=master)](https://coveralls.io/github/syin3/crash4viz?branch=master)
[![Build Status](https://travis-ci.com/syin3/crash4viz.svg?branch=master)](https://travis-ci.com/syin3/crash4viz)

This is a project of CSE583 by Katharine Chen, Tianqi Fang, Yutong Liu, Shuyi Yin.

## Goal
**Crash4viz** is an online platform that integrates various sources related to highway crashes in Washington State over the last 5 years. This tool facilitates visualization, exploration and analysis by average driver, professional users and professional developers.

## Technology Review
Our technology review introduces problem background, general use cases, data sets and initial data wrangling. It is online at [technology review](
https://syin3.github.io/WA-Crash-Viz-and-Analysis/technology%20review/#/).

## Organization of the  project

The project has the following structure:

    |-- crash4viz
        |-- .coveragerc
        |-- .travis.yml
        |-- LICENSE
        |-- README.md
        |-- interface.py
        |-- requirements-dev.txt
        |-- requirements.txt
        |-- setup.py
        |-- crash4viz
        |   |-- __init__.py
        |   |-- folium.ipynb
        |   |-- folium.py
        |   |-- mapping.py
        |   |-- mapping_funcs.py
        |   |-- mlpredict.py
        |   |-- dataprep
        |   |   |-- coords_conversion.ipynb
        |   |   |-- coords_conversion.py
        |   |   |-- create-sample.ipynb
        |   |   |-- create-sample.py
        |   |   |-- merge.ipynb
        |   |   |-- merge.py
        |   |   |-- obsolete-wrangle.ipynb
        |   |   |-- xlsx2csv.ipynb
        |   |   |-- xlsx2csv.py
        |   |-- milepost
        |   |   |-- plot-milepost.ipynb
        |   |   |-- plot-milepost.py
        |   |-- tests
        |       |-- __init__.py
        |       |-- test_mapping.py
        |       |-- test_mapping_funcs.py
        |       |-- test_ml.py
        |       |-- test_data
        |       |   |-- sample.csv
        |       |-- test_output
        |           |-- Weather_basic_map_test.html
        |           |-- Weather_cluster_map_test.html
        |           |-- Weather_layer_cluster_map_test.html
        |           |-- Weather_layer_map_test.html
        |-- data
        |   |-- coords-noaa
        |   |   |-- 2013_coords_0.csv
        |   |   |-- 2013_coords_1.csv
        |   |   |-- 2013_coords_2.csv
        |   |   |-- 2014_coords_0.csv
        |   |   |-- 2014_coords_1.csv
        |   |   |-- 2014_coords_2.csv
        |   |   |-- 2014_coords_3.csv
        |   |   |-- 2015_coords_0.csv
        |   |   |-- 2015_coords_1.csv
        |   |   |-- 2015_coords_2.csv
        |   |   |-- 2015_coords_3.csv
        |   |   |-- 2016_coords_0.csv
        |   |   |-- 2016_coords_1.csv
        |   |   |-- 2016_coords_2.csv
        |   |   |-- 2016_coords_3.csv
        |   |   |-- 2017_coords_0.csv
        |   |   |-- 2017_coords_1.csv
        |   |   |-- 2017_coords_2.csv
        |   |   |-- 2017_coords_3.csv
        |   |-- coords2convert
        |   |   |-- acc_13_0.csv
        |   |   |-- acc_13_1.csv
        |   |   |-- acc_13_10.csv
        |   |   |-- acc_13_2.csv
        |   |   |-- acc_13_3.csv
        |   |   |-- acc_13_4.csv
        |   |   |-- acc_13_5.csv
        |   |   |-- acc_13_6.csv
        |   |   |-- acc_13_7.csv
        |   |   |-- acc_13_8.csv
        |   |   |-- acc_13_9.csv
        |   |   |-- acc_14_0.csv
        |   |   |-- acc_14_1.csv
        |   |   |-- acc_14_10.csv
        |   |   |-- acc_14_11.csv
        |   |   |-- acc_14_12.csv
        |   |   |-- acc_14_2.csv
        |   |   |-- acc_14_3.csv
        |   |   |-- acc_14_4.csv
        |   |   |-- acc_14_5.csv
        |   |   |-- acc_14_6.csv
        |   |   |-- acc_14_7.csv
        |   |   |-- acc_14_8.csv
        |   |   |-- acc_14_9.csv
        |   |   |-- acc_15_0.csv
        |   |   |-- acc_15_1.csv
        |   |   |-- acc_15_10.csv
        |   |   |-- acc_15_11.csv
        |   |   |-- acc_15_12.csv
        |   |   |-- acc_15_13.csv
        |   |   |-- acc_15_2.csv
        |   |   |-- acc_15_3.csv
        |   |   |-- acc_15_4.csv
        |   |   |-- acc_15_5.csv
        |   |   |-- acc_15_6.csv
        |   |   |-- acc_15_7.csv
        |   |   |-- acc_15_8.csv
        |   |   |-- acc_15_9.csv
        |   |   |-- acc_16_0.csv
        |   |   |-- acc_16_1.csv
        |   |   |-- acc_16_10.csv
        |   |   |-- acc_16_11.csv
        |   |   |-- acc_16_12.csv
        |   |   |-- acc_16_13.csv
        |   |   |-- acc_16_14.csv
        |   |   |-- acc_16_2.csv
        |   |   |-- acc_16_3.csv
        |   |   |-- acc_16_4.csv
        |   |   |-- acc_16_5.csv
        |   |   |-- acc_16_6.csv
        |   |   |-- acc_16_7.csv
        |   |   |-- acc_16_8.csv
        |   |   |-- acc_16_9.csv
        |   |   |-- acc_17_0.csv
        |   |   |-- acc_17_1.csv
        |   |   |-- acc_17_10.csv
        |   |   |-- acc_17_11.csv
        |   |   |-- acc_17_12.csv
        |   |   |-- acc_17_13.csv
        |   |   |-- acc_17_2.csv
        |   |   |-- acc_17_3.csv
        |   |   |-- acc_17_4.csv
        |   |   |-- acc_17_5.csv
        |   |   |-- acc_17_6.csv
        |   |   |-- acc_17_7.csv
        |   |   |-- acc_17_8.csv
        |   |   |-- acc_17_9.csv
        |   |-- crash-merged
        |   |   |-- 2013.csv
        |   |   |-- 2014.csv
        |   |   |-- 2015.csv
        |   |   |-- 2016.csv
        |   |   |-- 2017.csv
        |   |-- hsis
        |   |   |-- wa13acc.xlsx
        |   |   |-- wa13curv.xlsx
        |   |   |-- wa13grad.xlsx
        |   |   |-- wa13occ.xlsx
        |   |   |-- wa13road.xlsx
        |   |   |-- wa13veh.xlsx
        |   |   |-- wa14acc.xlsx
        |   |   |-- wa14curv.xlsx
        |   |   |-- wa14grad.xlsx
        |   |   |-- wa14occ.xlsx
        |   |   |-- wa14road.xlsx
        |   |   |-- wa14veh.xlsx
        |   |   |-- wa15acc.xlsx
        |   |   |-- wa15curv.xlsx
        |   |   |-- wa15grad.xlsx
        |   |   |-- wa15occ.xlsx
        |   |   |-- wa15road.xlsx
        |   |   |-- wa15veh.xlsx
        |   |   |-- wa16acc.xlsx
        |   |   |-- wa16curv.xlsx
        |   |   |-- wa16grad.xlsx
        |   |   |-- wa16occ.xlsx
        |   |   |-- wa16road.xlsx
        |   |   |-- wa16veh.xlsx
        |   |   |-- wa17acc.xlsx
        |   |   |-- wa17curv.xlsx
        |   |   |-- wa17grad.xlsx
        |   |   |-- wa17occ.xlsx
        |   |   |-- wa17road.xlsx
        |   |   |-- wa17veh.xlsx
        |   |-- hsis-csv
        |   |   |-- wa13acc.csv
        |   |   |-- wa13curv.csv
        |   |   |-- wa13grad.csv
        |   |   |-- wa13occ.csv
        |   |   |-- wa13road.csv
        |   |   |-- wa13veh.csv
        |   |   |-- wa14acc.csv
        |   |   |-- wa14curv.csv
        |   |   |-- wa14grad.csv
        |   |   |-- wa14occ.csv
        |   |   |-- wa14road.csv
        |   |   |-- wa14veh.csv
        |   |   |-- wa15acc.csv
        |   |   |-- wa15curv.csv
        |   |   |-- wa15grad.csv
        |   |   |-- wa15occ.csv
        |   |   |-- wa15road.csv
        |   |   |-- wa15veh.csv
        |   |   |-- wa16acc.csv
        |   |   |-- wa16curv.csv
        |   |   |-- wa16grad.csv
        |   |   |-- wa16occ.csv
        |   |   |-- wa16road.csv
        |   |   |-- wa16veh.csv
        |   |   |-- wa17acc.csv
        |   |   |-- wa17curv.csv
        |   |   |-- wa17grad.csv
        |   |   |-- wa17occ.csv
        |   |   |-- wa17road.csv
        |   |   |-- wa17veh.csv
        |   |-- milepost
        |       |-- SRMilepostMarkers.dbf
        |       |-- SRMilepostMarkers.htm
        |       |-- SRMilepostMarkers.prj
        |       |-- SRMilepostMarkers.sbn
        |       |-- SRMilepostMarkers.sbx
        |       |-- SRMilepostMarkers.shp
        |       |-- SRMilepostMarkers.shp.xml
        |       |-- SRMilepostMarkers.shx
        |       |-- SRMilepostMarkers.gdb
        |           |-- a00000001.TablesByName.atx
        |           |-- a00000001.gdbindexes
        |           |-- a00000001.gdbtable
        |           |-- a00000001.gdbtablx
        |           |-- a00000002.gdbtable
        |           |-- a00000002.gdbtablx
        |           |-- a00000003.gdbindexes
        |           |-- a00000003.gdbtable
        |           |-- a00000003.gdbtablx
        |           |-- a00000004.CatItemsByPhysicalName.atx
        |           |-- a00000004.CatItemsByType.atx
        |           |-- a00000004.FDO_UUID.atx
        |           |-- a00000004.freelist
        |           |-- a00000004.gdbindexes
        |           |-- a00000004.gdbtable
        |           |-- a00000004.gdbtablx
        |           |-- a00000004.spx
        |           |-- a00000005.CatItemTypesByName.atx
        |           |-- a00000005.CatItemTypesByParentTypeID.atx
        |           |-- a00000005.CatItemTypesByUUID.atx
        |           |-- a00000005.gdbindexes
        |           |-- a00000005.gdbtable
        |           |-- a00000005.gdbtablx
        |           |-- a00000006.CatRelsByDestinationID.atx
        |           |-- a00000006.CatRelsByOriginID.atx
        |           |-- a00000006.CatRelsByType.atx
        |           |-- a00000006.FDO_UUID.atx
        |           |-- a00000006.gdbindexes
        |           |-- a00000006.gdbtable
        |           |-- a00000006.gdbtablx
        |           |-- a00000007.CatRelTypesByBackwardLabel.atx
        |           |-- a00000007.CatRelTypesByDestItemTypeID.atx
        |           |-- a00000007.CatRelTypesByForwardLabel.atx
        |           |-- a00000007.CatRelTypesByName.atx
        |           |-- a00000007.CatRelTypesByOriginItemTypeID.atx
        |           |-- a00000007.CatRelTypesByUUID.atx
        |           |-- a00000007.gdbindexes
        |           |-- a00000007.gdbtable
        |           |-- a00000007.gdbtablx
        |           |-- a00000009.gdbindexes
        |           |-- a00000009.gdbtable
        |           |-- a00000009.gdbtablx
        |           |-- a00000009.spx
        |           |-- gdb
        |           |-- timestamps
        |-- docs
        |   |-- pre-final pre.pdf
        |   |-- data handbook
        |   |   |-- hsis_data_guidebook.pdf
        |   |   |-- var_explanation.pdf
        |   |-- design docs
        |   |   |-- functional specification.md
        |   |   |-- software components.md
        |   |-- final pre
        |   |   |-- index.html
        |   |-- misc
        |   |   |-- get the data ready.ipynb
        |   |   |-- publish.sh
        |   |-- tech review
        |       |-- coords.ipynb
        |       |-- index.html
        |       |-- tech_pre.pdf
        |       |-- plots
        |       |   |-- bokeh_year_2014.html
        |       |   |-- bokeh_year_2015.html
        |       |   |-- bokeh_year_2016.html
        |       |   |-- bokeh_year_2017.html
        |       |   |-- folium_fats_by_county.html
        |       |   |-- folium_injuries_fats_by_county.html
        |       |   |-- folium_year.html
        |       |   |-- times.png
        |-- examples
        |   |-- EXAMPLES.md
        |   |-- interface.png
        |-- outputs
            |-- Adams_Weather_basic_map.html
            |-- light_plot.png
            |-- month_plot.png
            |-- road_plot.png
            |-- weather_factor_importance.png
            |-- weather_plot.png
            |-- weekday_plot.png
            |-- year_plot.png


## Install the program
To install this program, run:
1. ```git clone https://github.com/syin3/crash4viz.git```
2. ```cd crash4viz```
3. ```python setup.py install ```

## Graphical User Interface
To launch the crash visualization interface, run (from the top-level of the github repo):
```python3 interface.py```

Select the environmental, road, and incident type features you would like to visualize and press 'Show map', the interactable html map will be output into the directory ```outputs```.

## Tests
For users interested in testing the time to completion of each type of map, you can run (from the top-level of the github repo):
```python -m unittest crash4viz.tests.test_mapping```
Currently this will run timed tests for each type of map using a default selection of crash data features, which may differ slightly from feature to feature.

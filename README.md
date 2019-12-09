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
        |   |-- mapping.py
        |   |-- mapping_funcs.py
        |   |-- mlpredict.py
        |   |-- dataprep
        |   |   |-- s1-xlsx2csv.py
        |   |   |-- s2-coords_convert.py
        |   |   |-- s3-merge.py
        |   |   |-- s4-folium_prep.py
                |-- milepost
                        |-- plot-milepost.py
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
        |   |   |-- ...
        |   |-- coords2convert
        |   |   |-- ...
        |   |-- crash-merged
        |   |   |-- ...
        |   |-- hsis
        |   |   |-- ...
        |   |-- hsis-csv
        |   |   |-- ...
        |   |-- milepost
        |       |-- ...
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
        |   |   |-- ...
        |   |-- tech review
        |       |-- index.html
        |       |-- ...
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

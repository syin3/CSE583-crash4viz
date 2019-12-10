# Crash4viz
[![Coverage Status](https://coveralls.io/repos/github/syin3/crash4viz/badge.svg?branch=master&kill_cache=1)](https://coveralls.io/github/syin3/crash4viz?branch=master&kill_cache=1)
[![Build Status](https://travis-ci.com/syin3/crash4viz.svg?branch=master)](https://travis-ci.com/syin3/crash4viz)

This is a project of CSE583 by Katharine Chen, Tianqi Fang, Yutong Liu, Shuyi Yin.

## Goal
**Crash4viz** is an application that integrates various data sources of highway crash in Washington State over the last 5 years. This tool facilitates visualization, exploration and analysis by average driver and professional users.

## Technology Review
Our technology review introduces problem background, general use cases, data sets and initial data wrangling. It is online at [technology review](
https://syin3.github.io/crash4viz/docs/tech%20review/#/).

## Final Presentation
Our final presentation per request of [CSE583 project requirement](http://uwseds.github.io/projects.html) introduces project background, database design, use cases, design, structure and lessons learned. It is online at [final pre](
https://syin3.github.io/crash4viz/docs/final%20pre/).

## Organization of the  project

The project has the following structure:

    |-- crash4viz
        |-- interface.py
        |-- requirements.txt
        |-- setup.py
        |-- crash4viz
            |-- mapping.py
            |-- mapping_funcs.py
            |-- mlpredict.py
            |-- dataprep/
            |-- tests
                |-- test_mapping.py
                |-- test_mapping_funcs.py
                |-- test_ml.py
                |-- test_output/
        |-- data
            |-- hsis-csv/
            |-- crash-merged/
            |-- ...
        |-- docs
            |-- pre-final pre.pdf
            |-- examples/
            |-- data handbook/
            |-- design docs/
            |-- final pre/
            |-- tech review/
        |-- outputs/


## Install the program
To install this program, run:
1. ```git clone https://github.com/syin3/crash4viz.git```
2. ```cd crash4viz```
3. ```python setup.py install ```

## Graphical User Interface
To launch the crash visualization interface, run (from the top-level of the github repo):
```python3 interface.py```

Select the environmental, road, and incident type features you would like to visualize and press ***Show map***, the interactable html map will be output into the directory ```outputs```.

## Tests
For users interested in testing the time to completion of each type of map, you can run (from the top-level of the github repo):
```python -m unittest crash4viz.tests.test_mapping```
Currently this will run timed tests for each type of map using a default selection of crash data features, which may differ slightly from feature to feature.

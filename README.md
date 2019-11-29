# WA-Crash-Viz-and-Analysis
This is a project of CSE583 by Katharine Chen, Tianqi Fang, Yutong Liu, Shuyi Yin.

## Goal
**WA-Crash-Viz-and-Analysis** is an online platform that integrates various sources related to highway crashes in Washington State over the last 5 years. This tool facilitates visualization, exploration and analysis by average driver, professional users and professional developers.

## Technology Review
Our technology review introduces problem background, general use cases, data sets and initial data wrangling. It is online at [technology review](
https://syin3.github.io/WA-Crash-Viz-and-Analysis/technology%20review/#/).

## Install the program
To install this program, run:
1. ```git clone https://github.com/syin3/WA-Crash-Viz-and-Analysis.git```
2. ```cd WA-Crash-Viz-and-Analysis```
3. ```pip install . ``` --> not done yet, requires setup.py

## Graphical User Interface
To launch the crash visualization interface, run (from the top-level of the github repo):
```python3 interface.py```

Select the environmental, road, and incident type features you would like to visualize and press 'Show map', the interactable html map will be output into the directory MyMaps.

## Tests
For users interested in testing the time to completion of each type of map, you can run (from the top-level of the github repo):
```python -m unittest WAcrashviz.tests.test_mapping```
Currently this will run timed tests for each type of map using a default selection of crash data features, which may differ slightly from feature to feature.
"""Tests for generating the different map options available to users.
The output is the example map as well as a tsv file containing the time
it took to generate the map."""

import unittest
import os
import warnings
import time
import inspect
import sys
CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
PARENTDIR = os.path.dirname(CURRENTDIR)
PARENT = os.path.dirname(PARENTDIR)
sys.path.insert(0, PARENT)
from crash4viz import mapping
from crash4viz import mapping_funcs

TEST_OUTPUT = CURRENTDIR + '/test_output/'

class TestMapping(unittest.TestCase):
    """Test the different map options we have, the inputs to these mapping
    functions are set within each function, so will differ slightly for
    different features.
    """

    def setUp(self):
        warnings.simplefilter('ignore')

    def test_basic_map(self):

        """Use this test to assess how much time a basic map takes to
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the
         top-most level of the WAcrashviz package."""
        
        vars_dict = mapping_funcs.VARS_DICT
        subgroups_dict = mapping_funcs.R_SUBGROUPS_DICT
        incident_dict = mapping_funcs.R_INCIDENT_DICT
        county_dict = mapping_funcs.R_COUNTY_DICT

        test_year = '2013'
        test_county = county_dict['Adams']
        test_county_name = mapping_funcs.COUNTY_DICT[test_county]
        test_grp_feature = vars_dict['Weather']
        test_subgrp_feature = subgroups_dict['Weather']['Raining']

        test_df = mapping_funcs.read_dataframe(test_year)
        test_dataframe = test_df[test_df.COUNTY == test_county]
        test_group_df = test_dataframe.groupby(test_grp_feature)
        test_subgrp_df = test_group_df.apply(lambda g: g[g['weather'] == test_subgrp_feature])
        test_grp_dict = mapping_funcs.GRP_DICT
        test_group = test_grp_dict[test_grp_feature]

        testmap = mapping.Maps()
        map_sink = TEST_OUTPUT + f'{test_group}_basic_map_test.html'
        t_zero = time.time()
        testmap.basic_map(
            test_county_name,
            test_county,
            test_group,
            test_dataframe,
            test_subgrp_df,
            map_sink)
        t_one = time.time()

        total = t_one - t_zero
        time_to_generate = 'basic map generation time is ' + str(total)
        
        save_tsv = TEST_OUTPUT + 'generation_times.tsv'
        with open(save_tsv, 'a+') as output:
            output.write(time_to_generate)

    def test_cluster_map(self):

        """Use this test to assess how much time a cluster map takes to
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the
         top-most level of the WAcrashviz package."""
        
        vars_dict = mapping_funcs.VARS_DICT
        subgroups_dict = mapping_funcs.R_SUBGROUPS_DICT
        incident_dict = mapping_funcs.R_INCIDENT_DICT
        county_dict = mapping_funcs.R_COUNTY_DICT

        test_year = '2013'
        test_county = county_dict['Adams']
        test_county_name = mapping_funcs.COUNTY_DICT[test_county]
        test_grp_feature = vars_dict['Weather']
        test_subgrp_feature = subgroups_dict['Weather']['Raining']

        test_df = mapping_funcs.read_dataframe(test_year)
        test_dataframe = test_df[test_df.COUNTY == test_county]
        test_group_df = test_dataframe.groupby(test_grp_feature)
        test_subgrp_df = test_group_df.apply(lambda g: g[g['weather'] == test_subgrp_feature])
        test_grp_dict = mapping_funcs.GRP_DICT
        test_group = test_grp_dict[test_grp_feature]

        testmap = mapping.Maps()
        map_sink = TEST_OUTPUT + f'{test_group}_cluster_map_test.html'
        t_zero = time.time()

        testmap.plot_folium_filtered_clusters(
            test_county_name,
            test_county,
            test_group,
            test_dataframe,
            test_subgrp_df,
            map_sink)
        t_one = time.time()

        total = t_one - t_zero
        time_to_generate = 'cluster map generation time is ' + str(total)

        save_tsv = TEST_OUTPUT + 'generation_times.tsv'
        with open(save_tsv, 'a+') as output:
            output.write(time_to_generate)

    def test_layer_map(self):

        """Use this test to assess how much time a layer map takes to
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the
         top-most level of the WAcrashviz package."""
        
        vars_dict = mapping_funcs.VARS_DICT
        subgroups_dict = mapping_funcs.R_SUBGROUPS_DICT
        incident_dict = mapping_funcs.R_INCIDENT_DICT
        county_dict = mapping_funcs.R_COUNTY_DICT

        test_year = '2013'
        test_county = county_dict['Adams']
        test_county_name = mapping_funcs.COUNTY_DICT[test_county]
        test_grp_feature = vars_dict['Weather']
        test_subgrp_feature = subgroups_dict['Weather']['Raining']

        test_df = mapping_funcs.read_dataframe(test_year)
        test_dataframe = test_df[test_df.COUNTY == test_county]
        test_group_df = test_dataframe.groupby(test_grp_feature)
        test_subgrp_df = test_group_df.apply(lambda g: g[g['weather'] == test_subgrp_feature])
        test_grp_dict = mapping_funcs.GRP_DICT
        test_group = test_grp_dict[test_grp_feature]

        testmap = mapping.Maps()
        map_sink = TEST_OUTPUT + f'{test_group}_layer_map_test.html'
        t_zero = time.time()

        testmap.plot_folium_filtered_layers(
            test_group,
            test_county_name,
            test_county,
            test_grp_feature,
            test_subgrp_feature,
            map_sink)
        t_one = time.time()

        total = t_one - t_zero
        time_to_generate = 'layer map generation time is ' + str(total)
        save_tsv = TEST_OUTPUT + 'generation_times.tsv'
        with open(save_tsv, 'a+') as output:
            output.write(time_to_generate)

    def test_layer_cluster_map(self):

        """Use this test to assess how much time the big map takes to
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the
         top-most level of the WAcrashviz package."""
        
        vars_dict = mapping_funcs.VARS_DICT
        subgroups_dict = mapping_funcs.R_SUBGROUPS_DICT
        incident_dict = mapping_funcs.R_INCIDENT_DICT
        county_dict = mapping_funcs.R_COUNTY_DICT

        test_year = '2013'
        test_county = county_dict['Adams']
        test_county_name = mapping_funcs.COUNTY_DICT[test_county]
        test_grp_feature = vars_dict['Weather']
        test_subgrp_feature = subgroups_dict['Weather']['Raining']

        test_df = mapping_funcs.read_dataframe(test_year)
        test_dataframe = test_df[test_df.COUNTY == test_county]
        test_group_df = test_dataframe.groupby(test_grp_feature)
        test_subgrp_df = test_group_df.apply(lambda g: g[g['weather'] == test_subgrp_feature])
        test_grp_dict = mapping_funcs.GRP_DICT
        test_group = test_grp_dict[test_grp_feature]

        testmap = mapping.Maps()
        map_sink = TEST_OUTPUT + f'{test_group}_layer_cluster_map_test.html'
        t_zero = time.time()

        testmap.plot_folium_filtered_clusters_layers(
            test_county_name,
            test_county,
            test_group,
            test_grp_feature,
            test_subgrp_feature,
            map_sink)
        t_one = time.time()

        total = t_one - t_zero
        time_to_generate = 'layered cluster generation time is ' + str(total)
        save_tsv = TEST_OUTPUT + 'generation_times.tsv'
        with open(save_tsv, 'a+') as output:
            output.write(time_to_generate)

if __name__ == '__main__':
    unittest.main()

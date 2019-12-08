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
from wacrashviz import mapping
from wacrashviz import mapping_funcs

TEST_OUTPUT = CURRENTDIR + '/test_output/generation_times.tsv'

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

        r_incident_dict = mapping_funcs.R_INCIDENT_DICT
        grp_dict = mapping_funcs.GRP_DICT
        test_grp_feature = 'WEATHER'
        test_grp = grp_dict[test_grp_feature]
        test_subgrp_feature = 'Raining'
        test_incident_type = '# INJ'
        test_inc = r_incident_dict[test_incident_type]
        test_df = mapping_funcs.clean_dataframe()
        testmap = mapping.Maps()
        map_sink = CURRENTDIR + '/test_output/'
        map_sink = map_sink + f'{test_grp}_{test_inc}_basic_map_test.html'
        t_zero = time.time()
        testmap.basic_map(
            test_grp_feature,
            test_subgrp_feature,
            test_incident_type,
            test_df,
            map_sink)
        t_one = time.time()

        total = t_one - t_zero
        time_to_generate = 'basic map generation time is ' + str(total)


        with open(TEST_OUTPUT, 'a+') as output:
            output.write(time_to_generate)

    def test_cluster_map(self):

        """Use this test to assess how much time a cluster map takes to
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the
         top-most level of the WAcrashviz package."""

        r_incident_dict = mapping_funcs.R_INCIDENT_DICT
        grp_dict = mapping_funcs.GRP_DICT
        test_grp_feature = 'WEATHER'
        test_grp = grp_dict[test_grp_feature]
        test_subgrp_feature = 'Raining'
        test_incident_type = '# INJ'
        test_inc = r_incident_dict[test_incident_type]
        test_df = mapping_funcs.clean_dataframe()
        testmap = mapping.Maps()
        map_sink = CURRENTDIR + '/test_output/'
        map_sink = map_sink + f'{test_grp}_{test_inc}_cluster_map_test.html'
        t_zero = time.time()
        testmap.plot_folium_filtered_clusters(
            test_grp_feature,
            test_subgrp_feature,
            test_incident_type,
            test_df,
            map_sink)
        t_one = time.time()

        total = t_one - t_zero
        time_to_generate = 'cluster map generation time is ' + str(total)

        with open(TEST_OUTPUT, 'a+') as output:
            output.write(time_to_generate)

    def test_layer_map(self):

        """Use this test to assess how much time a layer map takes to
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the
         top-most level of the WAcrashviz package."""

        r_incident_dict = mapping_funcs.R_INCIDENT_DICT
        grp_dict = mapping_funcs.GRP_DICT
        test_grp_feature = 'WEATHER'
        test_grp = grp_dict[test_grp_feature]
        test_subgrp_feature = 'Raining'
        test_incident_type = '# INJ'
        test_inc = r_incident_dict[test_incident_type]
        test_df = mapping_funcs.clean_dataframe()
        testmap = mapping.Maps()
        map_sink = CURRENTDIR + '/test_output/'
        map_sink = map_sink + f'{test_grp}_{test_inc}_layer_map_test.html'
        t_zero = time.time()
        testmap.plot_folium_filtered_layers(
            test_grp_feature,
            test_subgrp_feature,
            test_incident_type,
            test_df,
            map_sink)
        t_one = time.time()

        total = t_one - t_zero
        time_to_generate = 'layer map generation time is ' + str(total)

        with open(TEST_OUTPUT, 'a+') as output:
            output.write(time_to_generate)

    def test_gigantic_map(self):

        """Use this test to assess how much time the big map takes to
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the
         top-most level of the WAcrashviz package."""

        r_incident_dict = mapping_funcs.R_INCIDENT_DICT
        grp_dict = mapping_funcs.GRP_DICT
        test_grp_feature = 'WEATHER'
        test_grp = grp_dict[test_grp_feature]
        test_df = mapping_funcs.clean_dataframe()
        testmap = mapping.Maps()
        map_sink = CURRENTDIR + '/test_output/'
        map_sink = map_sink + f'{test_grp}_big_map_test.html'
        t_zero = time.time()
        testmap.plot_folium(
            test_grp_feature,
            test_df,
            map_sink)
        t_one = time.time()

        total = t_one - t_zero
        time_to_generate = 'gigantic map generation time is ' + str(total)

        with open(TEST_OUTPUT, 'a+') as output:
            output.write(time_to_generate)

if __name__ == '__main__':
    unittest.main()

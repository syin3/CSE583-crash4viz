import unittest
import os
import inspect
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parent = os.path.dirname(parentdir)
sys.path.insert(0,parent)
from WAcrashviz import mapping
from WAcrashviz import mapping_funcs
import warnings
import time

class TestMapping(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore')

    def test_basic_map(self):

        """Use this test to assess how much time a basic map takes to 
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the 
         top-most level of the WAcrashviz package."""
        
        r_incident_dict = mapping_funcs.r_incident_dict
        grp_dict = mapping_funcs.grp_dict
        test_grp_feature = 'WEATHER'
        test_grp = grp_dict[test_grp_feature]
        test_subgrp_feature = 'Raining'
        test_incident_type = '# INJ'
        test_inc = r_incident_dict[test_incident_type]
        test_df = mapping_funcs.clean_dataframe()
        testmap = mapping.Maps()
        map_sink = currentdir + '/test_output/'
        map_sink = map_sink + f'{test_grp}_{test_inc}_basic_map_test.html'
        t0 = time.time()
        testmap.basic_map(
            test_grp_feature,
            test_subgrp_feature,
            test_incident_type,
            test_df,
            map_sink)
        t1 = time.time()
        
        total = t1- t0
        time_to_generate = 'basic map generation time is ' + str(total)
            
        print(time_to_generate)
        
    def test_cluster_map(self):

        """Use this test to assess how much time a cluster map takes to 
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the 
         top-most level of the WAcrashviz package."""
        
        r_incident_dict = mapping_funcs.r_incident_dict
        grp_dict = mapping_funcs.grp_dict
        test_grp_feature = 'WEATHER'
        test_grp = grp_dict[test_grp_feature]
        test_subgrp_feature = 'Raining'
        test_incident_type = '# INJ'
        test_inc = r_incident_dict[test_incident_type]
        test_df = mapping_funcs.clean_dataframe()
        testmap = mapping.Maps()
        map_sink = currentdir + '/test_output/'
        map_sink = map_sink + f'{test_grp}_{test_inc}_cluster_map_test.html'
        t0 = time.time()
        testmap.plot_folium_filtered_clusters(
            test_grp_feature,
            test_subgrp_feature,
            test_incident_type,
            test_df,
            map_sink)
        t1 = time.time()
        
        total = t1- t0
        time_to_generate = 'cluster map generation time is ' + str(total)
            
        print(time_to_generate)
        
    def test_layer_map(self):

        """Use this test to assess how much time a layer map takes to 
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the 
         top-most level of the WAcrashviz package."""
        
        r_incident_dict = mapping_funcs.r_incident_dict
        grp_dict = mapping_funcs.grp_dict
        test_grp_feature = 'WEATHER'
        test_grp = grp_dict[test_grp_feature]
        test_subgrp_feature = 'Raining'
        test_incident_type = '# INJ'
        test_inc = r_incident_dict[test_incident_type]
        test_df = mapping_funcs.clean_dataframe()
        testmap = mapping.Maps()
        map_sink = currentdir + '/test_output/'
        map_sink = map_sink + f'{test_grp}_{test_inc}_layer_map_test.html'
        t0 = time.time()
        testmap.plot_folium_filtered_layers(
            test_grp_feature,
            test_subgrp_feature,
            test_incident_type,
            test_df,
            map_sink)
        t1 = time.time()
        
        total = t1- t0
        time_to_generate = 'layer map generation time is ' + str(total)
            
        print(time_to_generate)
        
        
    def test_gigantic_map(self):

        """Use this test to assess how much time the big map takes to 
        generate. However, this will vary depending on how much data belongs
         to the test_grp_feature and test_subgrp_feature. Run from the 
         top-most level of the WAcrashviz package."""
        
        r_incident_dict = mapping_funcs.r_incident_dict
        grp_dict = mapping_funcs.grp_dict
        test_grp_feature = 'WEATHER'
        test_grp = grp_dict[test_grp_feature]
        test_df = mapping_funcs.clean_dataframe()
        testmap = mapping.Maps()
        map_sink = currentdir + '/test_output/'
        map_sink = map_sink + f'{test_grp}_big_map_test.html'
        t0 = time.time()
        testmap.plot_folium(
            test_grp_feature,
            test_df,
            map_sink)
        t1 = time.time()
        
        total = t1- t0
        time_to_generate = 'gigantic map generation time is ' + str(total)
            
        print(time_to_generate)

if __name__ == '__main__':
    unittest.main()
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

class TestMapping(unittest.TestCase):

    def test_basic_map(self):

        """Use this test to assess how much time a basic map takes to 
        generate. Run from the top-most level of the WAcrashviz package."""
        
        r_incident_dict = mapping_funcs.r_incident_dict
        test_grp_feature = 'WEATHER'
        test_subgrp_feature = 'Raining'
        test_incident_type = '# INJ'
        test_df = mapping_funcs.clean_dataframe()
        testmap = mapping.Maps()
        testmap.basic_map(
            test_grp_feature,
            test_subgrp_feature,
            test_incident_type,
            test_df)


if __name__ == '__main__':
    unittest.main()

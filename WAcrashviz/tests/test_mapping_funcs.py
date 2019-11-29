import unittest
import os
import inspect
import sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parent = os.path.dirname(parentdir)
sys.path.insert(0,parent)
from WAcrashviz import mapping_funcs
import warnings

class TestMappingFuncs(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore')

    """Tests for ensuring elements of the data are loaded correctly. 
    Run these tests from the top-most directory of the WAcrashviz package."""
    
    def test_clean_dataframe(self):
        df = mapping_funcs.clean_dataframe()

        num_columns = 16
        
        self.assertEqual(len(df.columns), 16,
                         "Dataframe not wrangled correctly")

    def test_paths(self):

        self.assertRegex(mapping_funcs.MODULE_DIR, 'WAcrashviz',
                               "Path to WAcrashviz module is incorrect")
        
        self.assertRegex(mapping_funcs.MAPS_DIR, '/MyMaps',
                               "Maps are not being saved in MyMaps directory")

        self.assertRegex(mapping_funcs.DATA_DIR, '/data/',
                               "Path to HSIS crash data is incorrect")

if __name__ == '__main__':
    unittest.main()
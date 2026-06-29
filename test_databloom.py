# test_databloom.py
"""
Tests for DataBloom module.
"""

import unittest
from databloom import DataBloom

class TestDataBloom(unittest.TestCase):
    """Test cases for DataBloom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataBloom()
        self.assertIsInstance(instance, DataBloom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataBloom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

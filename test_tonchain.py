# test_tonchain.py
"""
Tests for TonChain module.
"""

import unittest
from tonchain import TonChain

class TestTonChain(unittest.TestCase):
    """Test cases for TonChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TonChain()
        self.assertIsInstance(instance, TonChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TonChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

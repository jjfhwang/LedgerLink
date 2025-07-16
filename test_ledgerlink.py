# test_ledgerlink.py
"""
Tests for LedgerLink module.
"""

import unittest
from ledgerlink import LedgerLink

class TestLedgerLink(unittest.TestCase):
    """Test cases for LedgerLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LedgerLink()
        self.assertIsInstance(instance, LedgerLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LedgerLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

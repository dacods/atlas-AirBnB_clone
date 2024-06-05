#!/usr/bin/python3
"""Test for the Amenity Class"""
import unittest
from models.amenity import Amenity


class Test_amenity(unittest.TestCase):
    """Testing amenity"""
    def setUp(self):
        self.amenity = Amenity()

    def test_amenity(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_amenity_values(self):
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")
        self.amenity.name = "name"
        self.assertEqual(self.amenity.name, "name")

if __name__ == "__main__":
    unittest.main()
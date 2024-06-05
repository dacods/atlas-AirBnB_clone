#!/usr/bin/python3
"""Test for the City Class"""
import unittest
from models.city import City


class Test_city(unittest.TestCase):
    """Testing city"""
    def setUp(self):
        self.city = City()

    def test_city(self):
        self.assertIsInstance(self.city, City)
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))

    def test_city_value(self):
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

if __name__ == "__main__":
    unittest.main()
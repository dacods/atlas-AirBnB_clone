#!/usr/bin/python3
"""Test for the Place Class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Testing Place"""
    def setUp(self):
        self.place = Place()

    def test_place(self):
        self.assertIsInstance(self.place, Place)
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))

    def test_place_values(self):
        """Testing values"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")

if __name__ == "__main__":
    unittest.main()
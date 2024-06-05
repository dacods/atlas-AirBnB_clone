#!/usr/bin/python3
"""Test for the Review Class"""
import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """Testing Review"""
    def setUp(self):
        self.review = Review()

    def test_review(self):
        self.assertIsInstance(self.review, Review)
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))

    def test_review_values(self):
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

if __name__ == "__main__":
    unittest.main()
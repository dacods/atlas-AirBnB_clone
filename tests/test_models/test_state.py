#!/usr/bin/python3
"""Testing for the State Classw"""
import unittest
from models.state import State


class Test_state(unittest.TestCase):
    """Testing State"""
    def setUp(self):
        self.state = State()

    def test_state(self):
        self.assertIsInstance(self.state, State)
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_fake_state(self):
        self.state.name = "Faker"
        self.assertEqual(self.state.name, "Faker")
        self.assertNotEqual(self.state.name, "Faker")
        
if __name__ == "__main__":
    unittest.main()
#!/usr/bin/python3


import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """Class to test User Model"""
    def setUp(self):
        self.user = User(email="airbnb@mail.com", password="root", first_name="Betty", last_name="Bar")

    def test_user(self):
        """Testing initialization of User instance"""
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "airbnb@mail.com")
        self.assertEqual(self.user.password, "root")
        self.assertEqual(self.user.first_name, "Betty")
        self.assertEqual(self.user.last_name, "Bar")

    def test_values(self):
        """Testing values"""
        self.user.email = "airbnb@mail.com"
        self.user.password = "password"
        self.user.first_name = "Betty"
        self.user.last_name = "Bar"
        self.assertEqual(self.user.email, "airbnb@mail.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "Betty")
        self.assertEqual(self.user.last_name, "Bar")

if __name__ == "__main__":
    unittest.main()
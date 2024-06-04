#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserModel(unittest.TestCase):
    """Class to test User Model"""
    def setUp(self):
        self.user = User()

    def test_user(self):
        """Testing initialization of User instance"""
        self.assertIsInstance(self.user, User)
        self.assertTrue(hasattr(self.user, "airbnb@mail.com"))
        self.assertTrue(hasattr(self.user, "root"))
        self.assertTrue(hasattr(self.user, "Betty"))
        self.assertTrue(hasattr(self.user, "Bar"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

if __name__ == "__main__":
    unittest.main()

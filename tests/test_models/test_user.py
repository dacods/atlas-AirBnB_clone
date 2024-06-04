#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserModel(unittest.TestCase):
    """Class to test User Model"""
    def setUp(self):
        self.user = User(email="airbnb@mail.com", password="root", first_name="Betty", last_name="Bar")

    def test_user(self):
        """Testing initialization of User instance"""
        self.assertEqual(self.user.email, "airbnb@mail.com")
        self.assertEqual(self.user.password, "root")
        self.assertEqual(self.user.first_name, "Betty")
        self.assertEqual(self.user.last_name, "Bar")

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Tests for BaseModel"""

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Unittests for testing BaseModel"""
    def test_base_save(self):
        model = BaseModel()
        model.save()
        updated_at = model.updated_at
        self.assertIsInstance(updated_at, datetime)

if __name__ == '__main__':
    unittest.main()

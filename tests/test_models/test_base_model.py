#!/usr/bin/python3
import sys
import os
import unittest
from time import sleep
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))


class TestBaseModel(unittest.TestCase):
    maxDiff = None  # Allow full diff to be shown

    def test_save(self):
        model = BaseModel()
        initial_updated_at = model.updated_at
        sleep(0.1) 
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(initial_updated_at, new_updated_at)
        self.assertTrue(new_updated_at > initial_updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)

    def test_id(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertTrue(model.created_at.isoformat() in model.to_dict().get('created_at'))

    def test_str(self):
        model = BaseModel()
        model_str = str(model)
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model_str, expected_str, f"Expected: {expected_str}\nActual: {model_str}")

if __name__ == '__main__':
    unittest.main()
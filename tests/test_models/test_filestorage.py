#!/usr/bin/python3
"""Test for the FileStoarge Class"""
import json, os, unittest
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_filestorage(unittest.TestCase):
    """Testing FileStorage"""
    def setUp(self):
        self.instace = FileStorage()
        self.obj = BaseModel()
        self.path = "file.json"
        if os.path.exists(self.path):
            with open(self.path, 'r') as f:
                self.before_save = json.load(f)
        else:
            self.before_save = {}

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_save(self):
        self.instace.all()["New"] = self.obj
        self.instace.save()

        with open(self.path, 'r') as f:
            after_save = json.load(f)

        self.assertNotEqual(self.before_save, after_save)

    def test_new_and_all(self):
        new_obj = BaseModel()
        tmp_storage = FileStorage
        tmp_storage.new(new_obj)
        all_obj = tmp_storage.all()
        obj_key = f"{new_obj.__class__.__name__}.{new_obj.id}"
        self.assertIn(obj_key, all_obj)
        self.assertEqual(all_obj[obj_key], new_obj)

if __name__ == "__main__":
    unittest.main()
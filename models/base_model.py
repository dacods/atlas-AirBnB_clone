#!/usr/bin/python3
"""Module for BaseModel"""


import uuid
from datetime import datetime


class BaseModel:
    """Initializing BaseModel"""
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)

    def __str__(self):
        """Function to print the string rep of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}]"

    def save(self):
        """Function to update the updated_ at attribute
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Function to return the dictionary containing the keys and values"""
        data_dict = self.__dict__.copy()
        data_dict['created_at'] = self.created_at.isoformat()
        data_dict['updated_at'] = self.updated_at.isoformat()
        data_dict['__class__'] = self.__class__.__name__
        return data_dict

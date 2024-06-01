#!/bin/usr/python3
"""Module for User Class"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class defining the public class attrs"""
    email = ""
    password = ""
    first_name = ""
    last_name: ""

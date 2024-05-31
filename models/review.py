#!/usr/bin/python3
"""Module for Review Class"""


from models.base_model import BaseModel


class Review(BaseModel):
    """Class for Review instance attributes"""
    place_id = ""
    user_id = ""
    text = ""

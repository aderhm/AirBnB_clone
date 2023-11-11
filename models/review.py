#!/usr/bin/python3
"""
    module for the class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        the class Review
    """
    place_id = ""
    user_id = ""
    text = ""

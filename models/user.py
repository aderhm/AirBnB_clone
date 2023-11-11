#!/usr/bin/env python3
"""
    model for the user
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
        the class User, create a new object user
        and add a new attribute class
    """

    email = ""
    first_name = ""
    last_name = ""
    password = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

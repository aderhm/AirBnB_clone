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
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
            initialize of the object user
        """
        super().__init__(*args, **kwargs)

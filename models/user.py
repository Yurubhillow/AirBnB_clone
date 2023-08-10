#!/usr/bin/python3
"""Defines a user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user class
       Attr:
            ::email(str): A str holding users email.
            ::password(str): str holding users password.
            ::first_name(str): str holding users first name.
            ::last_name: str holding the users last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

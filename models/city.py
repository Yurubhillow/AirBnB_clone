#!/usr/bin/python3
"""Defines the 'City' class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents the city field.

    Attributes:
        state_id(str): The unique ID for each state.
        name(str): The name of the city we are looking at.
    """

    state_id = ""
    name = ""

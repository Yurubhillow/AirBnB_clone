#!/usr/bin/python3
"""Defines the class 'Review'."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents the review section.

    Attributes:
        place_id(str): the ID of the place being reviewed.
        user_id(str): the ID of the user leaving a review.
        text(str): the text description of the written review.
    """

    place_id = ""
    user_id = ""
    text = ""

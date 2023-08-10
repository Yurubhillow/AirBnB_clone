#!/usr/bin/python3
"""Defines the 'Place' class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents the input field of 'place'.

    Attributes:
        city_id(str): the unique ID of the city.
        user_id(str): the user ID
        name(str): the name of the place.
        description(str): the place description
        number_rooms(int): the number of rooms available in that place.
        number_bathrooms(int): the number of bathrooms in that place.
        max_guest(int): the maximum number of guests allowed in that place.
        price_by_night(int): the nightly charges for that place
        latitude(float): the latitude of the place.
        longitude(float): the longitude of the place.
        amenity_ids(list: the list of amenity IDs.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

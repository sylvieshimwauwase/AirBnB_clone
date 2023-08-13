#!/usr/bin/python3
"""defining place class that inherits from basemodel"""


class Place(BaseModel):
    """representing place class"""

    def __init__(self, *args, **kwargs):
        """defining plave attributes"""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

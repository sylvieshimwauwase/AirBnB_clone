#!/usr/bin/python3
"""defining review class inherited from basemodel"""


class Review(BaseModel):
    """representing review class"""

    def __init__(self, *args, **kwargs):
        """defining review attributes"""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

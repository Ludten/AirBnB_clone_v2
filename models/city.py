#!/usr/bin/python3
""" City Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.state import State
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models.place import Place
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def places(self):
            """Get places for FileStorage"""
            from models.place import Place
            from models import storage
            place_dict = storage.all(Place)
            place_list = list(place_dict.values())
            return [place for place in place_list if place.city_id == self.id]

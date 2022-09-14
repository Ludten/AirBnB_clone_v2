#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity


class Amenity(BaseModel, Base):
    """ Amenities different places have """
    __tablename__ = 'amenities'
    name = Column(String(1024), nullable=False)
    place_amenities = relationship(
        "Place", secondary=place_amenity, backref='places',
        viewonly=False)

#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
import models
import os


place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float2
        amenity_ids: list of Amenity ids
    """

    __tablename__ = 'places'
    city_id = Column(String(60),
                     ForeignKey('cities.id', ondelete='cascade'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id', ondelete='cascade'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship('Review',
                           cascade='delete', backref='place')
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False)
    @property
    def reviews(self):
        """getter attribute"""
        objs = models.storage.all(models.Review)
        return [v for v in objs.values() if self.id == v.place_id]

    @property
    def amenities(self):
        """getter attribute"""
        objs = models.storage.all('Amenity')
        return [amen for amen in objs.values() if amen.id in amenity_ids]

    @amenities.setter
    def amenities(self, obj):
        if isinstance(obj, Amenity):
            if self.id == obj.place_id:
                self.amenity_ids.append(obj.id)

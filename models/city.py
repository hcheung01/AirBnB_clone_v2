#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),
                          ForeignKey("states.id", ondelete='cascade'),
                          nullable=False)
        places = relationship("Place", cascade='delete', backref="cities")
    else:
        state_id = ""
        name = ""

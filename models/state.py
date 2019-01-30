#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='delete', backref="state")
    else:
        name = ""

        @property
        def cities(self):
            my_cities = models.storage.all(models.classes['City']).values()
            return [city for city in my_cities if city.state_id == self.id]

            """return list of all objects in storage
            return [v for k, v in models.storage.all(models.classes['City'])
                    .items()
                    if self.id == v.state_id]
            """

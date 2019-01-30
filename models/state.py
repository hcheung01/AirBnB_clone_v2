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
            """getter"""
            all_cities = models.storage.all(models.classes['City']).values()
            return [c for c in all_cities if c.state_id == self.id]

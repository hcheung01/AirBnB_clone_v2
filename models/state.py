#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", passive_deletes=True, backref="state")

    @property
    def cities(self):
        """ return list of all objects in storage"""
        return [v for k, v in models.storage.all().items()
                if self.id == v.state_id]

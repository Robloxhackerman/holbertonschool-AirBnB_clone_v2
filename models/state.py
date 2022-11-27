#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel):
    """ State class """
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """aaaa"""

            result = []

            for key in storage.all(City).values():
                if self.id == City.state_id:
                    result.append(storage.all(City)[key])
            return result
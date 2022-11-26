#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel):
    """ State class """

    __tablename__ = "states"
    
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',cascade='delete')

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """aaaa"""
            cities = []
            for cities in list(models.storage.all(City).values()):
                if cities.state_id == self.id:
                    cities.append(city)
            return cities
#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """ returns the list of City instances with state_id
        equals to the current State.id"""
        city_list = []
        cities = models.storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

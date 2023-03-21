#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Table, ForeignKey, DateTime
from models.city import City
from sqlalchemy.orm import relationship, backref


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                           cascade="all, delete-orphan")
    
    @property
    def cities(self):
        """returns list of city instances"""
        from models import storage
        return [v for k, v in storage.all(City).items()
                if v.state_id == self.id]

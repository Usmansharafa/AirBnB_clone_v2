#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Table, ForeignKey, Float
from sqlalchemy.orm import relationship, backref


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    
    reviews = relationship("Review", backref="place", cascade="all, delete")
    
    @property
    def reviews(self):
        """
        getter attribute reviews that returns the list of Review
        instances with place_id equals to the current Place.id
        """
        new_list = []
        query = storage.all().items()
        for key, value in query:
            if self.id == value.place_id:
                new_list.append(value)
        return new_list
                

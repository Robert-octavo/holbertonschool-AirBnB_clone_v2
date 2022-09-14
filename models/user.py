#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base if (STORAGE == "db") else object):
    """This class defines a user by various attributes"""

    if STORAGE == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", cascade='all, delete', backref="user")
        reviews = relationship("Review", cascade='all, delete', backref="user")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

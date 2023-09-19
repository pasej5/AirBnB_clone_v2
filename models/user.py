#!/usr/bin/python3
"""This module defines a class User"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """
    User class to represent the users table in the database.
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

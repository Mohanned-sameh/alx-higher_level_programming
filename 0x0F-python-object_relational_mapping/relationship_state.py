#!/usr/bin/python3
"""
Class: State
links to the MySQL table states
attribute: id that represents a column of an auto-generated, unique integer,
that  cant be null and is a primary key
attribute: name that represents a column of a string with maximum 128
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Class State
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

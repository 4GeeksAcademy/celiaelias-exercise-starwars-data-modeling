import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False)
    email = Column(String(120), nullable=False)
    password = Column(String(30), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    age = Column(Integer)
    height = Column(Float)
    gender = Column(String(80))
    affiliation = Column(String(150))

class planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    mass = Column(Float)
    diameter = Column(Float)
    atmosphere = Column(Float)
    orbital_period_year = Column(Float)
    orbital_period_day = Column(Float)

class Favourite_planets(Base):
    __tablename__ = 'favourite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(planet)

class Favourite_characters(Base):
    __tablename__ = 'favourite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(character)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

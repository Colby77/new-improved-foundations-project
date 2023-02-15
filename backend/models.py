from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email= Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)

    characters = relationship('Character', back_populates='creator')


class Character(Base):
    __tablename__ = 'characters'

    character_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    is_private = Column(Boolean, default=True)
    name = Column(String, nullable=False)
    race = Column(String, nullable=False)
    char_class = Column(String, nullable=False)
    background = Column(String, nullable=False)
    strength = Column(Integer, nullable=False)
    dexterity = Column(Integer, nullable=False)
    constitution = Column(Integer, nullable=False)
    wisdom = Column(Integer, nullable=False)
    intelligence = Column(Integer, nullable=False)
    charisma = Column(Integer, nullable=False)
    skills = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    alignment = Column(String, nullable=False)

    creator = relationship('User', back_populates='characters')


# class Comment(Base):
#     __tablename__ = 'comments'

#     character_id = 
#     user_id = 
#     content = Column(String, nullable=False)
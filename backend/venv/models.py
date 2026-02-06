from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(50),index=True)
    password = Column(String(100))

class Donor(Base):
    __tablename__ = "donors"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(60))
    age = Column(Integer)
    gender = Column(String(50))
    blood_group = Column(String(50))
    city = Column(String(50))
    phone_number = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
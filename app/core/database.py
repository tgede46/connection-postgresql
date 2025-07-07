from sqlmodel import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABSE_URL='postgresql://user:password@localhost:5433/postgres'

engin=create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engin)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
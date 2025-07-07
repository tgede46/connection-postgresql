from app.core.database import Base,engin
from app.db.models import citation
from sqlmodel import SQLModel

def create_table():
    SQLModel.metadata.create_all(bind=engin)
from sqlmodel import SQLModel, Session, create_engine
from core.config import settings

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

from database.session import SessionLocal



Base = declarative_base()

# start connections

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()
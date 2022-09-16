from sqlmodel import SQLModel, Session, create_engine
from core.config import settings

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

""" This module contains session connection the database"""


# Enable this for Postgresql database connection

# SQLALCHEMY_DATABASE_URI = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True, pool_pre_ping=True)


# SQLite database connection
database_file = "blog.db"
connect_args = {"check_same_thread": False}

SQLALCHEMY_DATABASE_URI = f"sqlite:///{database_file}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, echo=True, connect_args=connect_args
)  # sqlite


# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

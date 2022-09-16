""" Import all Models, so that Base has them before being import by Alembic"""
from database.base_class import Base
from models.users import User
from models.blog import Blog

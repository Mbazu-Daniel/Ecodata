from sqlalchemy.orm import Session
from core.config import settings

# from schemas.users import UserCreate
import crud, schemas


"""make sure all SQL Alchemy models are imported (database.base) before initializing Database otherwise, SQL Alchemy might fail to initialize relationships properly for more details: 

https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
"""

def init_db(db: Session):
    
    """
    Tables should be created with Alembic Migrations But if you don't want to use migrations, create the tables un-commenting the next line
    """

    # Base.metadata.create_all(bind=engine)

    user = user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = user.createUser(db, obj_in=user_in) 
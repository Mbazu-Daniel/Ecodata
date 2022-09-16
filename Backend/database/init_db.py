from sqlalchemy.orm import Session
from core.config import settings

from schemas.users import UserCreate
from crud.crud_users import get_by_email, createUser


"""make sure all SQL Alchemy models are imported (database.base) before initializing Database otherwise, SQL Alchemy might fail to initialize relationships properly for more details: 

https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28
"""


def init_db(db: Session):

    """
    Tables should be created with Alembic Migrations But if you don't want to use migrations, create the tables un-commenting the next line
    """

    # Base.metadata.create_all(bind=engine)
    if settings.FIRST_SUPERUSER:
        super_user = user.get_by_email(db, email=settings.FIRST_SUPERUSER)
        if not super_user:
            user_in = UserCreate(
                first_name="Super",
                last_name="User",
                email=settings.FIRST_SUPERUSER,
                password=settings.FIRST_SUPERUSER_PASSWORD,
                is_superuser=True,
            )
            super_user = user.createUser(db, obj_in=user_in)
        else:
            logger.warning(
                "Skipping creating superuser. User with email "
                f"{FIRST_SUPERUSER} already exists. "
            )
    else:
        logger.warning(
            "Skipping creating superuser.  FIRST_SUPERUSER needs to be "
            "provided as an env variable. "
            "e.g.  FIRST_SUPERUSER=admin@api.superuser.com"
        )

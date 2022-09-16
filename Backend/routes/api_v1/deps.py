from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session
from models.users import User
from core.security import verify_access_token
from core.config import settings
from database.session import SessionLocal
from crud.crud_users import user

# authentication scheme
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login/access-token"
)


# start database connections


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


""" Current authenticated user """


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(token, credentials_exception)
    user = db.query(User).filter(User.id == token.id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user


""" Current active user"""


def get_current_active_user(active_user: User = Depends(get_current_user)):
    if not user.is_active(active_user):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Inactive User"
        )

    return active_user


""" Current active superuser"""


def get_current_active_superuser(super_user: User = Depends(get_current_user)):
    if not user.is_superuser(super_user):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not not have superuser permission",
        )
    return super_user

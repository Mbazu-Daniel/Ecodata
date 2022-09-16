from datetime import datetime, timedelta
from typing import Any, Union
from fastapi import HTTPException, status, Depends
from core.config import settings
from jose import jwt
from passlib.context import CryptContext
from jose import JWTError
from pydantic import ValidationError
from schemas.token import TokenPayload

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None):
    if expires_delta:
        expire = datetime.utcnow()
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload = {"exp": expire, "sub": str(subject)}

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return token


""" This function is used to decode the access token created"""


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)  # what does it mean to add ** in Python

    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    # user = users.get_one(db, id=token_data.sub)
    #
    # if not user:
    #     raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "User not authorized")
    return token_data


""" Creating Hash and Verifying hash """


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def create_password_hash(password: str):
    return pwd_context.hash(password)

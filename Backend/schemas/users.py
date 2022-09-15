from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

date = datetime.now()


# Shared Properties for Users
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: bool = False
    created_at: datetime


# Properties to receive via API on creation
class UserCreate(UserBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "djangodaniel97@gmail.com",
                "password": "Password#123",
                "is_active": True,
                "is_superuser": False,
                "created_at": date
            }
        }


# Properties to receive via API on Login
class UserSignInSchema(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {"email": "djangodaniel97@gmail.com", "password": "Password#123"}
        }


""" You need to understand this Boy"""


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class UserOut(UserInDBBase):
    pass

# # Additional properties stored in DB
# class UserInDB(UserInDBBase):
#     hashed_password: str

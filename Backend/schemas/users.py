from pydantic import BaseModel, EmailStr

class User(BaseModel):
    full_name: str
    email: str
    password: str


    class Config:
        schema_extra = {
            "example": {
                "full_name": "John Doe",
                "email": "djangodaniel97@gmail.com",
                "password": "Password#123"
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "djangodaniel97@gmail.com",
                "password": "Password#123"
            }
        }
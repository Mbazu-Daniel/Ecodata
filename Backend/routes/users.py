from fastapi import APIRouter, HTTPException, status
from schemas.users import User, UserSignIn

user_router = APIRouter(tags=["User"], prefix="/user")

""" Create User Authentication """

users = {}

@user_router.post("/register")
async def create_user(data: User):
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with email {data.email} already exists",
        )
    users[data.email] = data

    return {"message": "User successfully registered!!!"}


@user_router.post("/login")
async def login_user(user: UserSignIn):
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exists"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials passed"
        )

    return {"message": "User signed in successfully"}

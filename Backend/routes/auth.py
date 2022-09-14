from fastapi import APIRouter, HTTPException, status
from schemas.users import UserCreateSchema, UserSignInSchema

auth_router = APIRouter(tags=["Authentication"])

""" Create User Authentication """

users = {}


@auth_router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user(data: UserCreateSchema):
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with email {data.email} already exists",
        )
    users[data.email] = data

    return {"message": "User successfully registered!!!"}


@auth_router.post("/login", status_code=status.HTTP_202_ACCEPTED)
async def login_user(user: UserSignInSchema):
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User does not exists"
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Wrong credentials passed"
        )

    return {"message": "User signed in successfully"}

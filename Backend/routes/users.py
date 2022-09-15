from fastapi import APIRouter, HTTPException, status
from schemas.users import UserCreate, UserOut, UserSignInSchema

user_router = APIRouter(tags=["User"])

""" Create User Profile Details """

users = {}

# @user_router.get("/{id}", response_model = UserOut)
# def get_user(id: int):
#     for user in users:
#         if user.id == id:
#             return user
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"user with supplied id {id} does not exist",
#     )

@user_router.get("/")
def get_user():
    return users
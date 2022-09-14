from fastapi import APIRouter, status, Body, HTTPException
from schemas.blog import BlogSchema
from typing import List

post_router = APIRouter(tags=["Post"], prefix="/post")

posts = []

""" CRUD (Create, Read, Update, Delete) OPERATION FOR THE POST ROUTER """


# CREATE Post Endpoints
@post_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(body: BlogSchema = Body(...)):
    posts.append(body)
    return {"message": "Post created successfully"}


# READ Post Endpoints
@post_router.get("/", response_model=List[BlogSchema])
async def get_all_post():
    return posts


@post_router.get("/{id}", response_model=BlogSchema)
async def retrieve_single_post(id: int):
    for post in posts:
        if post.id == id:
            return post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with supplied id {id} does not exist",
    )


# UPDATE Post Endpoint
# @post_router.put("/{id}")
# async def update_post(id: int, new_data: BlogUpdate):
#     for post in posts:
#         if post.id == id:
#             todo.

#         return posts
# raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"Post with supplied id {id} does not exist"
#     )

# DELETE Post Endpoint
@post_router.delete("/{id}")
async def delete_post(id: int):
    for post in posts:
        if post.id == id:
            posts.remove(post)
            return {"message": f"Post with ID {id} deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with supplied id {id} does not exist",
    )

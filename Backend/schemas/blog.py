from pydantic import BaseModel
from typing import Optional, List


# Shared properties
class BlogBase(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    image: Optional[str] = None
    published: bool = True


# Blog creation schema
class BlogCreate(BlogBase):
    title: str
    body: str
    image: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Introduction to Economics",
                "image": "https://linktomyimage.com/image.png",
                "body": "Economics is the study of the nations wealth",
                "published": True,
            }
        }

    #


class BlogUpdate(BlogBase):
    pass

    class Config:
        schema_extra = {
            "example": {
                "title": "Introduction to Economics",
                "image": "https://linktomyimage.com/image.png",
                "tags": ["Economics", "Micro Economics", "Macro Economics"],
                "body": "Economics is the study of the nations wealth",
                "published": True,
            }
        }


""" Blog data stored in the database"""

# Properties shared by models stored in DB
class BlogInDBBase(BlogBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties stored in DB
class BlogInDB(BlogInDBBase):
    pass


# Properties to return to client
class BlogSchema(BlogInDBBase):
    pass

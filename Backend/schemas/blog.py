from pydantic import BaseModel
from typing import Optional, List

class Blog(BaseModel):
    id: int
    title: str
    image: str
    body: str
    tags: List[str]
    author: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Introduction to Economics",
                "image": "https://linktomyimage.com/image.png",
                "tags": ["Economics", "Micro Economics", "Macro Economics"],
                "body": "Economics is the study of the nations wealth"
            }
        }
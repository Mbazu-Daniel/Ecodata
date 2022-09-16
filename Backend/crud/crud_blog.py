from crud.base import CRUDBase
from fastapi.encoders import jsonable_encoder
from models.blog import Blog
from schemas.blog import BlogUpdate, BlogCreate
from sqlalchemy.orm import Session


class CRUDItem(CRUDBase[Blog, BlogCreate, BlogUpdate]):
    def create_with_owner(self, db: Session, *, obj_in: BlogCreate, owner_id: int):
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ):
        return (
            db.query(self.model)
            .first(Blog.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


blog = CRUDItem(Blog)

from typing import Any, Dict, Optional, Union
from core.security import create_password_hash, verify_hash, verify_password
from models.users import User
from schemas.users import UserCreate, UserUpdate
from sqlalchemy.orm import Session
from crud.base import CRUDBase


class CRUDUser(CRUDBase[User,UserCreate,UserUpdate]):
    def get_by_email(self, db: Session, *, email: str):
        return db.query(User).filter(User.email == email).first()
    
    
    
    def createUser(self, db: Session, *, obj_in: UserCreate):
        db_obj = User(
            email = obj_in.email, hashed_password = create_password_hash(obj_in.password),
            first_name = obj_in.first_name,
            last_name = obj_in.last_name,
            is_superuser = obj_in.is_superuser
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def updateUser(self,db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]):
        if isinstance(obj_in, dict ):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        if update_data["password"]:
            hashed_password = create_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        return super().update(db, db_obj=db_obj, obj_in=update_data)


    def authenticate(self, db: Session, *, email: str, password: str):
        user = self.get_by_email(db, email=email)

        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active

    def is_superuser(self, user: User) -> bool:
            return user.is_superuser


user = CRUDUser(User)
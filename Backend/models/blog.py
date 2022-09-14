from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from database.connection import Base


class Blog(Base):
    id = Column(Integer, primary_key=True, index=True, nullable=False, server_default="gen_random_uuid()")
    title = Column(String, index=True, nullable=False)
    body = Column(String, index=True, nullable=False)
    image = Column(String, index=True, nullable=False)
    published = Column(Boolean, server_default="TRUE", nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="blog")

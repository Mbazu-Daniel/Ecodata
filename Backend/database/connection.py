from sqlmodel import SQLModel, Session, create_engine
from core.config import settings

database_file = "blog.db"
connect_args = {"check_same_thread": False}
# database_connection_string = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# engine = create_engine(database_connection_string, echo=True)

database_connection_string = f"sqlite:///{database_file}"
engine = create_engine(database_connection_string, echo=True, connect_args=connect_args) # sqlite



def conn():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

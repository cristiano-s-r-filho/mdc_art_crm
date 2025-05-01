from sqlmodel import SQLModel, Session, create_engine 
from .config import settings

engine = create_engine(settings.DATABASE_URL)

def get_db():
    with Session(engine) as session:
        yield session
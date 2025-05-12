from sqlmodel import SQLModel, create_engine

sqlite_url = "sqlite:///shopping_list.db"
engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
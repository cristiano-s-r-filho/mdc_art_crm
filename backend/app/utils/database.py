from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker
from app.models.ingredient import Ingredient
from app.models.recipe import Recipe
from app.models.menu import Menu
from app.models.recipe_ingredient import RecipeIngredient 

sqlite_url = "sqlite:///mdc_app.db"
engine = create_engine(sqlite_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False  # Critical fix
)

def get_db():
    with SessionLocal() as session:
        yield session    
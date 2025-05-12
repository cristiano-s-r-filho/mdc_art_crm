from fastapi import FastAPI
from app.routes import ingredients, recipes, menus
from app.utils.database import create_db_and_tables

app = FastAPI()

app.include_router(ingredients.router)
app.include_router(recipes.router)
app.include_router(menus.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
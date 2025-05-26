from fastapi import FastAPI
from app.routes import ingredients_router, recipes_router, menus_router
from app.utils.database import create_db_and_tables

app = FastAPI()

app.include_router(ingredients_router)
app.include_router(recipes_router)
app.include_router(menus_router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
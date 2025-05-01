from fastapi import FastAPI
from sqlmodel import SQLModel
from app.core.config import settings
from app.core.database import engine
from app.api.v1 import auth, recipes, menus

app = FastAPI(title="Recipe Manager API")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(recipes.router, prefix="/api/v1/recipes", tags=["Recipes"])
app.include_router(menus.router, prefix="/api/v1/menus", tags=["Menus"])

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
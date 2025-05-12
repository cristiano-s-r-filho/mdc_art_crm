from fastapi import APIRouter
from sqlmodel import Session
from app.models.ingredient import Ingredient, IngredientCreate, IngredientRead
from app.utils.database import engine

router = APIRouter(prefix="/api/ingredients")

@router.post("/", response_model=IngredientRead)
async def create_ingredient(ingredient: IngredientCreate):
    with Session(engine) as session:
        db_ingredient = Ingredient.model_validate(ingredient)
        session.add(db_ingredient)
        session.commit()
        session.refresh(db_ingredient)
        return db_ingredient
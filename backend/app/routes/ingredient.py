from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models.ingredient import Ingredient, IngredientCreate, IngredientRead, IngredientUpdate
from app.utils.database import engine, get_db

router = APIRouter(prefix="/api/ingredients")

@router.post("/create", response_model=IngredientRead)
async def create_ingredient(ingredient: IngredientCreate):
    with Session(engine) as session:
        db_ingredient = Ingredient.model_validate(ingredient)
        session.add(db_ingredient)
        session.commit()
        session.refresh(db_ingredient)
        return db_ingredient

@router.get("/all", response_model=list[IngredientRead])
async def read_ingredients(name: str = None):
    with Session(engine) as session:
        query = select(Ingredient)
        if name:
            query = query.where(Ingredient.name.contains(name))
        return session.execute(query).all()

@router.get("/{ingredient_id}", response_model=IngredientRead)
async def read_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = db.get(Ingredient, ingredient_id)
    if not ingredient:
        raise HTTPException(404, "Ingredient not found")
    return ingredient

@router.patch("/{ingredient_id}", response_model=IngredientRead)
async def update_ingredient(
    ingredient_id: int, 
    ingredient_data: IngredientUpdate,
    db: Session = Depends(get_db)
):
    db_ingredient = db.get(Ingredient, ingredient_id)
    if not db_ingredient:
        raise HTTPException(404, "Ingredient not found")
    
    update_dict = ingredient_data.dict(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(db_ingredient, key, value)
    
    db.add(db_ingredient)
    db.commit()
    db.refresh(db_ingredient)
    return db_ingredient

@router.delete("/{ingredient_id}")
async def delete_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = db.get(Ingredient, ingredient_id)
    if not ingredient:
        raise HTTPException(404, "Ingredient not found")
    db.delete(ingredient)
    db.commit()
    return {"deleted": True}
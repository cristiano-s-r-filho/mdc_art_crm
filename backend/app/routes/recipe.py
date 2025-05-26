from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from app.models.recipe import Recipe, RecipeCreate, RecipeRead, RecipeUpdate
from app.models.ingredient import Ingredient 
from app.models.recipe_ingredient import RecipeIngredient
from app.utils.database import get_db

router = APIRouter(prefix="/api/recipes")

@router.post("/create", response_model=RecipeRead)
async def create_recipe(
    recipe: RecipeCreate,
    db: Session = Depends(get_db)  # Use dependency injection
):
    try:
        # Create base recipe
        db_recipe = Recipe.model_validate(recipe)
        db.add(db_recipe)
        db.commit()
        db.refresh(db_recipe)  # Refresh while session is active
        
        # Add ingredients
        for ingredient_data in recipe.ingredients:
            ingredient = db.get(Ingredient, ingredient_data.ingredient_id)
            if not ingredient:
                raise HTTPException(404, f"Ingredient {ingredient_data.ingredient_id} not found")
            
            db.add(RecipeIngredient(
                recipe_id=db_recipe.id,
                ingredient_id=ingredient.id,
                quantity=ingredient_data.quantity
            ))
        
        db.commit()
        db.refresh(db_recipe)  # Final refresh before returning
        
        return db_recipe
    
    finally:
        db.close()  # Ensure session closure

@router.get("/all", response_model=list[RecipeRead])
async def read_recipes(name: str = None, db: Session = Depends(get_db)):
    query = select(Recipe)
    if name:
        query = query.where(Recipe.name.contains(name))
    result = db.execute(query)
    return result.scalars().all()

@router.get("/{recipe_id}", response_model=RecipeRead)
async def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.get(Recipe, recipe_id)
    if not recipe:
        raise HTTPException(404, "Recipe not found")
    return recipe

@router.patch("/{recipe_id}", response_model=RecipeRead)
async def update_recipe(
    recipe_id: int,
    recipe_data: RecipeUpdate,
    db: Session = Depends(get_db)
):
    db_recipe = db.get(Recipe, recipe_id)
    if not db_recipe:
        raise HTTPException(404, "Recipe not found")
    
    update_dict = recipe_data.dict(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(db_recipe, key, value)
    
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@router.delete("/{recipe_id}")
async def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.get(Recipe, recipe_id)
    if not recipe:
        raise HTTPException(404, "Recipe not found")
    db.delete(recipe)
    db.commit()
    return {"deleted": True}
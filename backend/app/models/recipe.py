from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from app.models.menu_recipe import MenuRecipe
from app.models.recipe_ingredient import RecipeIngredient, RecipeIngredientCreate

class RecipeBase(SQLModel):
    name: str = Field(index=True)
    description: Optional[str] = None

class Recipe(RecipeBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    recipe_ingredients: List["RecipeIngredient"] = Relationship(back_populates="recipe")
    menu_recipes: List["MenuRecipe"] = Relationship(back_populates="recipe")

class RecipeCreate(RecipeBase):
    ingredients: List[RecipeIngredientCreate] 
class RecipeRead(RecipeBase):
    id: int

class RecipeUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None

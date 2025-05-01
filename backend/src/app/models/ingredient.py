from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from app.models.base import BaseModel
from app.models.recipe import Recipe

class IngredientBase(SQLModel):
    name: str
    quantity: float 
    unit: str
    unit_cost: float = Field(description="Cost per unit")

class Ingredient(IngredientBase, BaseModel, table=True):
    recipe_id: int = Field(foreign_key="recipe.id")
    recipe: Recipe = Relationship(back_populates="ingredients")

class IngredientCreate(IngredientBase):
    pass
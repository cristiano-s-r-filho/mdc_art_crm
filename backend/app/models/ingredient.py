from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

class IngredientBase(SQLModel):
    name: str = Field(index=True, unique=True)
    unit: str
    unit_price: float

class Ingredient(IngredientBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # Fix relationship definition
    recipe_ingredients: List["RecipeIngredient"] = Relationship(back_populates="ingredient")
class IngredientCreate(IngredientBase):
    pass

class IngredientRead(IngredientBase):
    id: int

class IngredientUpdate(SQLModel):
    name: Optional[str] = None
    unit: Optional[str] = None
    unit_price: Optional[float] = None

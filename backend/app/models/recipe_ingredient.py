from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class RecipeIngredient(SQLModel, table=True):
    recipe_id: Optional[int] = Field(
        default=None, 
        foreign_key="recipe.id", 
        primary_key=True
    )
    ingredient_id: Optional[int] = Field(
        default=None, 
        foreign_key="ingredient.id", 
        primary_key=True
    )
    quantity: float
    
    # Fix back_populates references
    recipe: "Recipe" = Relationship(back_populates="recipe_ingredients")
    ingredient: "Ingredient" = Relationship(back_populates="recipe_ingredients")

class RecipeIngredientCreate(SQLModel):
    ingredient_id: int
    quantity: float
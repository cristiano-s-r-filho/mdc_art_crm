from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class MenuRecipe(SQLModel, table=True):
    menu_id: Optional[int] = Field(
        default=None, 
        foreign_key="menu.id", 
        primary_key=True
    )
    recipe_id: Optional[int] = Field(
        default=None, 
        foreign_key="recipe.id", 
        primary_key=True
    )
    
    menu: "Menu" = Relationship(back_populates="menu_recipes")
    recipe: "Recipe" = Relationship(back_populates="menu_recipes")
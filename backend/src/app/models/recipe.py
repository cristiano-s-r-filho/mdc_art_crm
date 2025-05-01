from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship
from typing import List
from app.models.base import BaseModel
from app.models.user import User
from app.models.ingredient import Ingredient
from app.models.menu import Menu

class RecipeBase(SQLModel):
    name: str
    owner_id: int = Field(foreign_key="user.id")

class Recipe(RecipeBase, BaseModel, table=True):
    owner: User = Relationship(back_populates="recipes")
    ingredients: List[Ingredient] = Relationship(back_populates="recipe")
    menus: List[Menu] = Relationship(
        back_populates="recipes", 
        link_model=MenuRecipeAssociation
    )

class RecipeCreate(RecipeBase):
    pass
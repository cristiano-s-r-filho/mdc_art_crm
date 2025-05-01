from sqlmodel import SQLModel, Field, Relationship
from typing import List
from .base import BaseModel

class MenuBase(SQLModel):
    name: str
    owner_id: int = Field(foreign_key="user.id")

class Menu(MenuBase, BaseModel, table=True):
    owner: "User" = Relationship(back_populates="menus")
    recipes: List["Recipe"] = Relationship(back_populates="menus", link_model=MenuRecipeAssociation)

class MenuCreate(MenuBase):
    recipe_ids: List[int]
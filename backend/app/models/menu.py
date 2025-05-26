from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from app.models.menu_recipe import MenuRecipe

class MenuBase(SQLModel):
    name: str = Field(index=True)
    description: Optional[str] = None

class Menu(MenuBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    menu_recipes: List["MenuRecipe"] = Relationship(back_populates="menu")
class MenuCreate(MenuBase):
    pass

class MenuRead(MenuBase):
    id: int

class MenuUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None

from sqlmodel import SQLModel, Field

class IngredientBase(SQLModel):
    name: str
    unit: str  # g, kg, etc
    unit_price: float

class Ingredient(IngredientBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class IngredientCreate(IngredientBase):
    pass

class IngredientRead(IngredientBase):
    id: int
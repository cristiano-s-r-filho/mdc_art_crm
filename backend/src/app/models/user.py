from sqlmodel import SQLModel, Field
from .base import BaseModel

class UserBase(SQLModel):
    email: str = Field(index=True, unique=True)
    password_hash: str

class User(UserBase, BaseModel, table=True):
    pass

class UserCreate(SQLModel):
    email: str
    password: str
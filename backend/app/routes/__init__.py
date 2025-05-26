from app.routes.ingredient import router as ingredients_router
from app.routes.recipe import router as recipes_router
from app.routes.menu import router as menus_router

__all__ = ["ingredients_router", "recipes_router", "menus_router"]
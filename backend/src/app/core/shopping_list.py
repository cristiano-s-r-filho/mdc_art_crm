from typing import List, Dict
from app.models import Ingredient
from app.models.menu import Menu
from app.models.recipe import Recipe
def aggregate_ingredients(recipes: List[Recipe]) -> List[Dict]:
    aggregated = {}
    for recipe in recipes:
        for ingredient in recipe.ingredients:
            key = (ingredient.name, ingredient.unit)
            if key not in aggregated:
                aggregated[key] = {
                    "name": ingredient.name,
                    "total_quantity": 0,
                    "unit": ingredient.unit,
                    "total_cost": 0
                }
            aggregated[key]["total_quantity"] += ingredient.quantity
            aggregated[key]["total_cost"] += ingredient.quantity * ingredient.unit_cost
    return list(aggregated.values())

def calculate_menu_cost(menu: Menu) -> float:
    return sum(
        ingredient.quantity * ingredient.unit_cost
        for recipe in menu.recipes
        for ingredient in recipe.ingredients
    )

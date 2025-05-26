from fastapi import APIRouter, HTTPException
from sqlmodel import Session, select
from app.models.menu import Menu
from app.utils.database import engine

router = APIRouter(prefix="/api/shopping")

@router.get("/{menu_id}")
async def get_shopping_list(menu_id: int):
    with Session(engine) as session:
        menu = session.get(Menu, menu_id)
        if not menu:
            raise HTTPException(status_code=404, detail="Menu not found")
        
        aggregated = {}
        total_cost = 0.0
        
        for recipe in menu.recipes:
            for ri in recipe.ingredients:
                ingredient = ri.ingredient
                key = f"{ingredient.id}-{ingredient.unit}"
                
                if key in aggregated:
                    aggregated[key]["quantity"] += ri.quantity
                else:
                    aggregated[key] = {
                        "name": ingredient.name,
                        "unit": ingredient.unit,
                        "quantity": ri.quantity,
                        "unit_price": ingredient.unit_price
                    }
                
                total_cost += ri.quantity * ingredient.unit_price
        
        return {
            "ingredients": list(aggregated.values()),
            "total_cost": round(total_cost, 2)
        }
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlmodel import Session, select
from app.core.database import get_db
from app.models.menu import Menu, MenuCreate
from app.models.recipe import Recipe
from app.core.shopping_list import aggregate_ingredients, calculate_menu_cost
from app.core.exporters import export_to_csv, export_to_excel, export_to_pdf

router = APIRouter()

@router.post("/menus/")
def create_menu(menu_data: MenuCreate, session: Session = Depends(get_db)):
    # Validate recipe IDs exist
    recipes = session.exec(select(Recipe).where(Recipe.id.in_(menu_data.recipe_ids))).all()
    if len(recipes) != len(menu_data.recipe_ids):
        raise HTTPException(status_code=404, detail="One or more recipes not found")
    
    # Create menu and associate recipes
    menu = Menu(name=menu_data.name, owner_id=1)  # Replace with auth user
    session.add(menu)
    session.commit()
    return menu

@router.get("/menus/{menu_id}/shopping-list")
def get_shopping_list(menu_id: int, session: Session = Depends(get_db)):
    menu = session.get(Menu, menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return aggregate_ingredients(menu.recipes)

@router.get("/menus/{menu_id}/export")
def export_shopping_list(
    menu_id: int, 
    format: str = "csv", 
    session: Session = Depends(get_db)
):
    menu = session.get(Menu, menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    
    shopping_list = aggregate_ingredients(menu.recipes)
    if format == "csv":
        return export_to_csv(shopping_list, "shopping_list.csv")
    elif format == "excel":
        return export_to_excel(shopping_list, "shopping_list.xlsx")
    elif format == "pdf":
        pdf_buffer = export_to_pdf(shopping_list, "shopping_list.pdf")
        return Response(content=pdf_buffer.read(), media_type="application/pdf")
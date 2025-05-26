from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.menu import Menu, MenuCreate, MenuRead, MenuUpdate
from app.models.menu_recipe import MenuRecipe # Ensure these exist
from app.utils.database import engine, get_db

router = APIRouter(prefix="/api/menus")  # Must be named 'router'

    
@router.post("/create", response_model=MenuRead)
async def create_menu(menu: MenuCreate, db: Session = Depends(get_db)):
    db_menu = Menu.model_validate(menu)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    
    # Add recipes
    for recipe_id in menu.recipe_ids:
        recipe = db.get(MenuRecipe, recipe_id)
        if not recipe:
            raise HTTPException(404, f"Recipe {recipe_id} not found")
        
        db.add(MenuRecipe(menu_id=db_menu.id, recipe_id=recipe_id))
    
    db.commit()
    return db_menu

@router.get("/all", response_model=list[MenuRead])
async def read_menus(name: str = None, db: Session = Depends(get_db)):
    query = select(Menu)
    if name:
        query = query.where(Menu.name.contains(name))
    return db.execute(query).all()

@router.get("/{menu_id}", response_model=MenuRead)
async def read_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = db.get(Menu, menu_id)
    if not menu:
        raise HTTPException(404, "Menu not found")
    return menu

@router.patch("/{menu_id}", response_model=MenuRead)
async def update_menu(
    menu_id: int,
    menu_data: MenuUpdate,
    db: Session = Depends(get_db)
):
    db_menu = db.get(Menu, menu_id)
    if not db_menu:
        raise HTTPException(404, "Menu not found")
    
    update_dict = menu_data.dict(exclude_unset=True)
    for key, value in update_dict.items():
        setattr(db_menu, key, value)
    
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu

@router.delete("/{menu_id}")
async def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    menu = db.get(Menu, menu_id)
    if not menu:
        raise HTTPException(404, "Menu not found")
    db.delete(menu)
    db.commit()
    return {"deleted": True}
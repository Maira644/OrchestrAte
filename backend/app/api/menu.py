from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.menu import MenuItemCreate, MenuItemResponse
from app.services.menu_service import (
    create_menu_item,
    get_all_menu_items,
    get_menu_item_by_id,
    update_menu_item,
    delete_menu_item,
)

router = APIRouter(
    prefix="/menu",
    tags=["Menu"]
)


@router.post("/", response_model=MenuItemResponse)
def create_menu(
    menu_item: MenuItemCreate,
    db: Session = Depends(get_db)
):
    return create_menu_item(db, menu_item)


@router.get("/", response_model=list[MenuItemResponse])
def get_menu(
    db: Session = Depends(get_db)
):
    return get_all_menu_items(db)


@router.get("/{menu_id}", response_model=MenuItemResponse)
def get_menu_item(
    menu_id: int,
    db: Session = Depends(get_db)
):
    menu_item = get_menu_item_by_id(db, menu_id)

    if not menu_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    return menu_item


@router.put("/{menu_id}", response_model=MenuItemResponse)
def update_menu(
    menu_id: int,
    menu_item: MenuItemCreate,
    db: Session = Depends(get_db)
):
    updated_item = update_menu_item(db, menu_id, menu_item)

    if not updated_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    return updated_item


@router.delete("/{menu_id}")
def delete_menu(
    menu_id: int,
    db: Session = Depends(get_db)
):
    deleted_item = delete_menu_item(db, menu_id)

    if not deleted_item:
        raise HTTPException(status_code=404, detail="Menu item not found")

    return {"message": "Menu item deleted successfully"}
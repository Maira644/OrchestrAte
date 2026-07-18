from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.inventory import InventoryCreate, InventoryResponse
from app.services.inventory_service import (
    create_inventory,
    get_all_inventory,
    get_inventory_by_id,
    update_inventory,
    delete_inventory,
)

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


@router.post("/", response_model=InventoryResponse)
def create_inventory_route(
    inventory: InventoryCreate,
    db: Session = Depends(get_db)
):
    return create_inventory(db, inventory)


@router.get("/", response_model=list[InventoryResponse])
def get_inventory(
    db: Session = Depends(get_db)
):
    return get_all_inventory(db)


@router.get("/{inventory_id}", response_model=InventoryResponse)
def get_inventory_item(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    inventory = get_inventory_by_id(db, inventory_id)

    if not inventory:
        raise HTTPException(status_code=404, detail="Inventory not found")

    return inventory


@router.put("/{inventory_id}", response_model=InventoryResponse)
def update_inventory_route(
    inventory_id: int,
    inventory: InventoryCreate,
    db: Session = Depends(get_db)
):
    updated = update_inventory(db, inventory_id, inventory)

    if not updated:
        raise HTTPException(status_code=404, detail="Inventory not found")

    return updated


@router.delete("/{inventory_id}")
def delete_inventory_route(
    inventory_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_inventory(db, inventory_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Inventory not found")

    return {"message": "Inventory deleted successfully"}
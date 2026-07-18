from sqlalchemy.orm import Session

from app.models.inventory import Inventory
from app.models.menu_item import MenuItem
from app.schemas.inventory import InventoryCreate


def create_inventory(db: Session, inventory: InventoryCreate):
    db_inventory = Inventory(
        menu_item_id=inventory.menu_item_id,
        current_stock=inventory.current_stock,
        minimum_stock=inventory.minimum_stock
    )

    db.add(db_inventory)

    # Update menu availability
    menu_item = db.query(MenuItem).filter(
        MenuItem.id == inventory.menu_item_id
    ).first()

    if menu_item:
        menu_item.stock = inventory.current_stock
        menu_item.available = inventory.current_stock > 0

    db.commit()
    db.refresh(db_inventory)

    return db_inventory


def get_all_inventory(db: Session):
    return db.query(Inventory).all()


def get_inventory_by_id(db: Session, inventory_id: int):
    return db.query(Inventory).filter(
        Inventory.id == inventory_id
    ).first()


def update_inventory(
    db: Session,
    inventory_id: int,
    inventory: InventoryCreate
):
    db_inventory = db.query(Inventory).filter(
        Inventory.id == inventory_id
    ).first()

    if not db_inventory:
        return None

    db_inventory.current_stock = inventory.current_stock
    db_inventory.minimum_stock = inventory.minimum_stock

    menu_item = db.query(MenuItem).filter(
        MenuItem.id == db_inventory.menu_item_id
    ).first()

    if menu_item:
        menu_item.stock = inventory.current_stock
        menu_item.available = inventory.current_stock > 0

    db.commit()
    db.refresh(db_inventory)

    return db_inventory


def delete_inventory(db: Session, inventory_id: int):
    db_inventory = db.query(Inventory).filter(
        Inventory.id == inventory_id
    ).first()

    if not db_inventory:
        return None

    db.delete(db_inventory)
    db.commit()

    return db_inventory
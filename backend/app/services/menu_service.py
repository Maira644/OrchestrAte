from sqlalchemy.orm import Session

from app.models.menu_item import MenuItem
from app.schemas.menu import MenuItemCreate


def create_menu_item(db: Session, menu_item: MenuItemCreate):
    db_menu_item = MenuItem(
        name=menu_item.name,
        category=menu_item.category,
        price=menu_item.price,
        stock=menu_item.stock,
        description=menu_item.description,
        image_url=menu_item.image_url,
    )

    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)

    return db_menu_item


def get_all_menu_items(db: Session):
    return db.query(MenuItem).all()

def get_menu_item_by_id(db: Session, menu_id: int):
    return db.query(MenuItem).filter(MenuItem.id == menu_id).first()


def update_menu_item(db: Session, menu_id: int, menu_item: MenuItemCreate):
    db_menu_item = db.query(MenuItem).filter(MenuItem.id == menu_id).first()

    if not db_menu_item:
        return None

    db_menu_item.name = menu_item.name
    db_menu_item.category = menu_item.category
    db_menu_item.price = menu_item.price
    db_menu_item.stock = menu_item.stock
    db_menu_item.description = menu_item.description
    db_menu_item.image_url = menu_item.image_url

    db.commit()
    db.refresh(db_menu_item)

    return db_menu_item


def delete_menu_item(db: Session, menu_id: int):
    db_menu_item = db.query(MenuItem).filter(MenuItem.id == menu_id).first()

    if not db_menu_item:
        return None

    db.delete(db_menu_item)
    db.commit()

    return db_menu_item
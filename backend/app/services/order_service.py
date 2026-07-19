from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.menu_item import MenuItem
from app.models.inventory import Inventory
from app.schemas.order import OrderCreate
from app.models.kitchen_ticket import KitchenTicket


def create_order(db: Session, order: OrderCreate):
    db_order = Order(
        customer_name=order.customer_name,
        status="Pending",
        total_price=0
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    total_price = 0

    for item in order.items:

        menu_item = db.query(MenuItem).filter(
            MenuItem.id == item.menu_item_id
        ).first()

        if not menu_item:
            continue

        order_item = OrderItem(
            order_id=db_order.id,
            menu_item_id=item.menu_item_id,
            quantity=item.quantity,
            price=menu_item.price
        )

        db.add(order_item)

        total_price += menu_item.price * item.quantity

        inventory = db.query(Inventory).filter(
            Inventory.menu_item_id == item.menu_item_id
        ).first()

        if inventory:
            inventory.current_stock -= item.quantity

            menu_item.stock = inventory.current_stock

            if inventory.current_stock <= 0:
                inventory.current_stock = 0
                menu_item.stock = 0
                menu_item.available = False

    db_order.total_price = total_price

    kitchen_ticket = KitchenTicket(
        order_id=db_order.id,
        status="Pending",
        priority=1,
        estimated_time=15
    )

    db.add(kitchen_ticket)

    db.commit()
    db.refresh(db_order)

    return db_order


def get_all_orders(db: Session):
    return db.query(Order).all()


def get_order_by_id(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def delete_order(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()

    if not order:
        return None

    db.delete(order)
    db.commit()

    return order
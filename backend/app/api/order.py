from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.order import OrderCreate, OrderResponse
from app.services.order_service import (
    create_order,
    get_all_orders,
    get_order_by_id,
    delete_order,
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/", response_model=OrderResponse)
def create_order_route(
    order: OrderCreate,
    db: Session = Depends(get_db)
):
    return create_order(db, order)


@router.get("/", response_model=list[OrderResponse])
def get_orders(
    db: Session = Depends(get_db)
):
    return get_all_orders(db)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = get_order_by_id(db, order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return order


@router.delete("/{order_id}")
def delete_order_route(
    order_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_order(db, order_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Order not found")

    return {"message": "Order deleted successfully"}
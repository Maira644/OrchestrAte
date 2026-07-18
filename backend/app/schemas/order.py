from pydantic import BaseModel, Field
from typing import List


class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: int = Field(..., gt=0)


class OrderCreate(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=100)
    items: List[OrderItemCreate]


class OrderItemResponse(BaseModel):
    id: int
    menu_item_id: int
    quantity: int
    price: float

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    id: int
    customer_name: str
    status: str
    total_price: float
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True
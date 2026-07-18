from pydantic import BaseModel, Field


class InventoryCreate(BaseModel):
    menu_item_id: int
    current_stock: int = Field(..., ge=0)
    minimum_stock: int = Field(..., ge=0)


class InventoryResponse(BaseModel):
    id: int
    menu_item_id: int
    current_stock: int
    minimum_stock: int

    class Config:
        from_attributes = True
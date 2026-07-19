from pydantic import BaseModel, Field


class KitchenTicketCreate(BaseModel):
    order_id: int
    priority: int = Field(default=1, ge=1, le=5)
    estimated_time: int = Field(default=15, ge=1)


class KitchenTicketUpdate(BaseModel):
    status: str


class KitchenTicketResponse(BaseModel):
    id: int
    order_id: int
    status: str
    priority: int
    estimated_time: int

    class Config:
        from_attributes = True
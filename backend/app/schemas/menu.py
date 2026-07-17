from pydantic import BaseModel


class MenuItemCreate(BaseModel):
    name: str
    category: str
    price: float
    stock: int
    description: str | None = None
    image_url: str | None = None


class MenuItemResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    stock: int
    available: bool
    description: str | None
    image_url: str | None

    class Config:
        from_attributes = True
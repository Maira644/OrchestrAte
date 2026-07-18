from pydantic import BaseModel, Field


class MenuItemCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    category: str = Field(..., min_length=2, max_length=50)
    price: float = Field(..., gt=0)
    stock: int = Field(..., ge=0)
    description: str | None = Field(default=None, max_length=500)
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
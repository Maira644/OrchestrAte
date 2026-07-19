from datetime import date, time

from pydantic import BaseModel, Field


class ReservationCreate(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=100)
    phone: str = Field(..., min_length=10, max_length=20)
    reservation_date: date
    reservation_time: time
    guests: int = Field(..., ge=1, le=20)
    table_number: int = Field(..., ge=1)


class ReservationUpdate(BaseModel):
    status: str


class ReservationResponse(BaseModel):
    id: int
    customer_name: str
    phone: str
    reservation_date: date
    reservation_time: time
    guests: int
    table_number: int
    status: str

    class Config:
        from_attributes = True
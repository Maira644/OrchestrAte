from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.reservation import (
    ReservationCreate,
    ReservationUpdate,
    ReservationResponse,
)
from app.services.reservation_service import (
    create_reservation,
    get_all_reservations,
    get_reservation_by_id,
    update_reservation_status,
    delete_reservation,
)

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)


@router.post("/", response_model=ReservationResponse)
def create_reservation_route(
    reservation: ReservationCreate,
    db: Session = Depends(get_db)
):
    created = create_reservation(db, reservation)

    if not created:
        raise HTTPException(
            status_code=400,
            detail="This table is already reserved for the selected date and time."
        )

    return created


@router.get("/", response_model=list[ReservationResponse])
def get_reservations(
    db: Session = Depends(get_db)
):
    return get_all_reservations(db)


@router.get("/{reservation_id}", response_model=ReservationResponse)
def get_reservation(
    reservation_id: int,
    db: Session = Depends(get_db)
):
    reservation = get_reservation_by_id(db, reservation_id)

    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    return reservation


@router.put("/{reservation_id}", response_model=ReservationResponse)
def update_reservation(
    reservation_id: int,
    reservation: ReservationUpdate,
    db: Session = Depends(get_db)
):
    updated = update_reservation_status(db, reservation_id, reservation)

    if not updated:
        raise HTTPException(status_code=404, detail="Reservation not found")

    return updated


@router.delete("/{reservation_id}")
def delete_reservation(
    reservation_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_reservation(db, reservation_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Reservation not found")

    return {"message": "Reservation deleted successfully"}
from sqlalchemy.orm import Session

from app.models.reservation import Reservation
from app.schemas.reservation import (
    ReservationCreate,
    ReservationUpdate,
)


def create_reservation(db: Session, reservation: ReservationCreate):
    existing = db.query(Reservation).filter(
        Reservation.table_number == reservation.table_number,
        Reservation.reservation_date == reservation.reservation_date,
        Reservation.reservation_time == reservation.reservation_time,
    ).first()

    if existing:
        return None

    db_reservation = Reservation(
        customer_name=reservation.customer_name,
        phone=reservation.phone,
        reservation_date=reservation.reservation_date,
        reservation_time=reservation.reservation_time,
        guests=reservation.guests,
        table_number=reservation.table_number,
    )

    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)

    return db_reservation


def get_all_reservations(db: Session):
    return db.query(Reservation).all()


def get_reservation_by_id(db: Session, reservation_id: int):
    return db.query(Reservation).filter(
        Reservation.id == reservation_id
    ).first()


def update_reservation_status(
    db: Session,
    reservation_id: int,
    reservation: ReservationUpdate,
):
    db_reservation = db.query(Reservation).filter(
        Reservation.id == reservation_id
    ).first()

    if not db_reservation:
        return None

    db_reservation.status = reservation.status

    db.commit()
    db.refresh(db_reservation)

    return db_reservation


def delete_reservation(db: Session, reservation_id: int):
    db_reservation = db.query(Reservation).filter(
        Reservation.id == reservation_id
    ).first()

    if not db_reservation:
        return None

    db.delete(db_reservation)
    db.commit()

    return db_reservation
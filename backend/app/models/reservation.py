from sqlalchemy import Column, Integer, String, Date, Time

from app.database.database import Base


class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(
        String,
        nullable=False
    )

    phone = Column(
        String,
        nullable=False
    )

    reservation_date = Column(
        Date,
        nullable=False
    )

    reservation_time = Column(
        Time,
        nullable=False
    )

    guests = Column(
        Integer,
        nullable=False
    )

    table_number = Column(
        Integer,
        nullable=False
    )

    status = Column(
        String,
        default="Confirmed"
    )
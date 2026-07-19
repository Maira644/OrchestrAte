from sqlalchemy.orm import Session

from app.models.kitchen_ticket import KitchenTicket
from app.schemas.kitchen import (
    KitchenTicketCreate,
    KitchenTicketUpdate,
)


def create_ticket(db: Session, ticket: KitchenTicketCreate):
    db_ticket = KitchenTicket(
        order_id=ticket.order_id,
        priority=ticket.priority,
        estimated_time=ticket.estimated_time,
    )

    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)

    return db_ticket


def get_all_tickets(db: Session):
    return db.query(KitchenTicket).all()


def get_ticket(db: Session, ticket_id: int):
    return db.query(KitchenTicket).filter(
        KitchenTicket.id == ticket_id
    ).first()


def update_ticket(
    db: Session,
    ticket_id: int,
    ticket: KitchenTicketUpdate,
):
    db_ticket = db.query(KitchenTicket).filter(
        KitchenTicket.id == ticket_id
    ).first()

    if not db_ticket:
        return None

    db_ticket.status = ticket.status

    db.commit()
    db.refresh(db_ticket)

    return db_ticket


def delete_ticket(db: Session, ticket_id: int):
    db_ticket = db.query(KitchenTicket).filter(
        KitchenTicket.id == ticket_id
    ).first()

    if not db_ticket:
        return None

    db.delete(db_ticket)
    db.commit()

    return db_ticket
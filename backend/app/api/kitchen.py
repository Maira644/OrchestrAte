from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.kitchen import (
    KitchenTicketCreate,
    KitchenTicketUpdate,
    KitchenTicketResponse,
)
from app.services.kitchen_service import (
    create_ticket,
    get_all_tickets,
    get_ticket,
    update_ticket,
    delete_ticket,
)

router = APIRouter(
    prefix="/kitchen",
    tags=["Kitchen"]
)


@router.post("/", response_model=KitchenTicketResponse)
def create_kitchen_ticket(
    ticket: KitchenTicketCreate,
    db: Session = Depends(get_db)
):
    return create_ticket(db, ticket)


@router.get("/", response_model=list[KitchenTicketResponse])
def get_kitchen_tickets(
    db: Session = Depends(get_db)
):
    return get_all_tickets(db)


@router.get("/{ticket_id}", response_model=KitchenTicketResponse)
def get_kitchen_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket = get_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(status_code=404, detail="Kitchen ticket not found")

    return ticket


@router.put("/{ticket_id}", response_model=KitchenTicketResponse)
def update_kitchen_ticket(
    ticket_id: int,
    ticket: KitchenTicketUpdate,
    db: Session = Depends(get_db)
):
    updated = update_ticket(db, ticket_id, ticket)

    if not updated:
        raise HTTPException(status_code=404, detail="Kitchen ticket not found")

    return updated


@router.delete("/{ticket_id}")
def delete_kitchen_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_ticket(db, ticket_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Kitchen ticket not found")

    return {"message": "Kitchen ticket deleted successfully"}
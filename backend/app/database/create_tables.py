from app.database.database import Base, engine

from app.models import (
    MenuItem,
    Inventory,
    Order,
    OrderItem,
    KitchenTicket,
    Reservation,
)

Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully!")
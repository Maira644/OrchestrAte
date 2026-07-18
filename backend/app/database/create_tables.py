from app.database.database import Base, engine

# Import all models
from app.models import (
    MenuItem,
    Inventory,
    Order,
    OrderItem,
)

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ All tables created successfully!")
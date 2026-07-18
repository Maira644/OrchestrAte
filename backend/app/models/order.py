from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String, nullable=False)

    status = Column(String, default="Pending")

    total_price = Column(Float, default=0)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete"
    )
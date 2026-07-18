from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)

    menu_item_id = Column(
        Integer,
        ForeignKey("menu_items.id"),
        unique=True,
        nullable=False
    )

    current_stock = Column(Integer, nullable=False)

    minimum_stock = Column(Integer, nullable=False)

    last_updated = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    menu_item = relationship("MenuItem")
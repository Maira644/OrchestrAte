from sqlalchemy import Boolean, Column, Float, Integer, String

from app.database.database import Base


class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    available = Column(Boolean, default=True)

    stock = Column(Integer, default=0)

    description = Column(String)

    image_url = Column(String)
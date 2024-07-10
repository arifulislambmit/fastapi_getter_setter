from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..db.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    _name = Column(String, index=True)
    _price = Column(Float)
    _description = Column(String, index=True, nullable=True)

    items = relationship("ProductItem", back_populates="product")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        self._price = price

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description
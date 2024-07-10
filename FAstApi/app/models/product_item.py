from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..db.database import Base

class ProductItem(Base):
    __tablename__ = "product_items"

    id = Column(Integer, primary_key=True, index=True)
    _name = Column(String, index=True)
    _quantity = Column(Integer)
    product_id = Column(Integer, ForeignKey('products.id'))

    product = relationship("Product", back_populates="items")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self._quantity = quantity
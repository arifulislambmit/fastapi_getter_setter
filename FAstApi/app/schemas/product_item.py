from pydantic import BaseModel

class ProductItemCreate(BaseModel):
    name: str
    quantity: int
    product_id: int

class ProductItemUpdate(BaseModel):
    name: str
    quantity: int

class ProductItemRead(BaseModel):
    id: int
    name: str
    quantity: int
    product_id: int

    class Config:
        orm_mode = True
        
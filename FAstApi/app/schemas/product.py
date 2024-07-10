from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str = None

class ProductUpdate(BaseModel):
    name: str
    price: float
    description: str = None

class ProductRead(BaseModel):
    id: int
    name: str
    price: float
    description: str = None

    class Config:
        orm_mode = True
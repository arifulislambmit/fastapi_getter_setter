from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..crud import product as crud_product
from ..schemas import product as schemas_product
from ..db.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/products/", response_model=schemas_product.ProductRead)
def create_product(product: schemas_product.ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create_product(db=db, product=product)

@router.get("/products/", response_model=List[schemas_product.ProductRead])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = crud_product.get_products(db, skip=skip, limit=limit)
    return products

@router.get("/products/{product_id}", response_model=schemas_product.ProductRead)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud_product.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/products/{product_id}", response_model=schemas_product.ProductRead)
def update_product(product_id: int, updated_product: schemas_product.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud_product.update_product(db=db, product_id=product_id, updated_product=updated_product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.delete("/products/{product_id}", response_model=schemas_product.ProductRead)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud_product.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..crud import product_item as crud_product_item
from ..schemas import product_item as schemas_product_item
from ..schemas.product_item import ProductItemCreate, ProductItemRead
from ..db.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.post("/product_items/", response_model=schemas_product_item.ProductItemRead)
# def create_product_item(product_item: schemas_product_item.ProductItemCreate, db: Session = Depends(get_db)):
#     return crud_product_item.create_product_item(db=db, product_item=product_item)
@router.post("/product_items/batch/", response_model=List[ProductItemRead])
def create_product_items_batch(product_items: List[ProductItemCreate], db: Session = Depends(get_db)):
    created_items = []
    for item in product_items:
        created_item = crud_product_item.create_product_item(db=db, product_item=item)
        created_items.append(created_item)
    return created_items



@router.get("/product_items/", response_model=List[schemas_product_item.ProductItemRead])
def read_product_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    product_items = crud_product_item.get_product_items(db, skip=skip, limit=limit)
    return product_items

@router.get("/product_items/{product_item_id}", response_model=schemas_product_item.ProductItemRead)
def read_product_item(product_item_id: int, db: Session = Depends(get_db)):
    db_product_item = crud_product_item.get_product_item(db, product_item_id=product_item_id)
    if db_product_item is None:
        raise HTTPException(status_code=404, detail="ProductItem not found")
    return db_product_item

@router.put("/product_items/{product_item_id}", response_model=schemas_product_item.ProductItemRead)
def update_product_item(product_item_id: int, updated_product_item: schemas_product_item.ProductItemUpdate, db: Session = Depends(get_db)):
    db_product_item = crud_product_item.update_product_item(db=db, product_item_id=product_item_id, updated_product_item=updated_product_item)
    if db_product_item is None:
        raise HTTPException(status_code=404, detail="ProductItem not found")
    return db_product_item

@router.delete("/product_items/{product_item_id}", response_model=schemas_product_item.ProductItemRead)
def delete_product_item(product_item_id: int, db: Session = Depends(get_db)):
    db_product_item = crud_product_item.delete_product_item(db=db, product_item_id=product_item_id)
    if db_product_item is None:
        raise HTTPException(status_code=404, detail="ProductItem not found")
    return db_product_item


from sqlalchemy.orm import Session
from ..models.product_item import ProductItem
from ..schemas.product_item import ProductItemCreate, ProductItemUpdate

def get_product_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ProductItem).offset(skip).limit(limit).all()

def get_product_item(db: Session, product_item_id: int):
    return db.query(ProductItem).filter(ProductItem.id == product_item_id).first()

# def create_product_item(db: Session, product_item: ProductItemCreate):
#     db_product_item = ProductItem(_name=product_item.name, _quantity=product_item.quantity, product_id=product_item.product_id)
#     db.add(db_product_item)
#     db.commit()
#     db.refresh(db_product_item)
#     return db_product_item

def create_product_item(db: Session, product_item: ProductItemCreate):
    db_product_item = ProductItem(**product_item.dict())
    db.add(db_product_item)
    db.commit()
    db.refresh(db_product_item)
    return db_product_item

def update_product_item(db: Session, product_item_id: int, updated_product_item: ProductItemUpdate):
    db_product_item = db.query(ProductItem).filter(ProductItem.id == product_item_id).first()
    if db_product_item:
        db_product_item.name = updated_product_item.name
        db_product_item.quantity = updated_product_item.quantity
        db.commit()
        db.refresh(db_product_item)
    return db_product_item

def delete_product_item(db: Session, product_item_id: int):
    db_product_item = db.query(ProductItem).filter(ProductItem.id == product_item_id).first()
    if db_product_item:
        db.delete(db_product_item)
        db.commit()
    return db_product_item
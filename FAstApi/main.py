from fastapi import FastAPI
from app.routes.router_list import router as api_router
from app.db.database import Base, engine

app = FastAPI()

# Create the tables
Base.metadata.create_all(bind=engine)

app.include_router(api_router)

'''
.
├── app
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── product_item.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── product_item.py
│   ├── db
│   │   ├── __init__.py
│   │   └── database.py
│   ├── crud
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   └── product_item.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── product.py
│   │   ├── product_item.py
│   │   └── router_list.py
├── main.py
└── requirements.txt

POST /api/product_items/batch/

[
    {"name": "Item 1", "quantity": 10},
    {"name": "Item 2", "quantity": 15},
    {"name": "Item 3", "quantity": 8}
]

[
  {
    "name": "string",
    "quantity": 0,
    "product_id": 0
  },
  {
    "name": "string",
    "quantity": 0,
    "product_id": 0
  }
]
'''
from fastapi import APIRouter

from . import user, product, product_item

router = APIRouter()

router.include_router(user.router, prefix="/api")
router.include_router(product.router, prefix="/api")
router.include_router(product_item.router, prefix="/api")
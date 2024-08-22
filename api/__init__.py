from fastapi import APIRouter

from .cars import router as cars_router
from .users import router as users_router

router = APIRouter(tags=["api"])

router.include_router(cars_router, prefix="/cars")
router.include_router(users_router, prefix="/users")

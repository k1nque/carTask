from fastapi import APIRouter

from .cars.views import router as cars_router
from .users.views import router as users_router

router = APIRouter()

router.include_router(cars_router, prefix="/cars")
router.include_router(users_router, prefix="/users")

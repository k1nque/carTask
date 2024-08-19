from fastapi import APIRouter

from .cars.views import router as cars_router

router = APIRouter()

router.include_router(cars_router, prefix="/cars")

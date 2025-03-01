from fastapi import APIRouter
from .customer.views import router as customer_router

api_router = APIRouter()
api_router.include_router(customer_router)
from fastapi import APIRouter

from .version1 import route_general_pages
from .version1 import route_user


api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router,prefix="",tags=["general_pages"])
api_router.include_router(route_user.router,prefix="/users",tags=["users"])
from api.v1 import route_debate
from api.v1 import route_login
from api.v1 import route_user
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route_user.router, prefix="", tags=["users"])
api_router.include_router(route_debate.router, prefix="", tags=["debates"])
api_router.include_router(route_login.router, prefix="", tags=["login"])

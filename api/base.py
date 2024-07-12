from fastapi import APIRouter

from api.v1 import route_user, route_debate

api_router = APIRouter()
api_router.include_router(route_user.router,prefix="/users",tags=["users"])
api_router.include_router(route_debate.router,prefix="/debates",tags=["debates"])
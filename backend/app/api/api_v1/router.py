from fastapi import APIRouter
from app.api.api_v1.handlers import user
from app.api.api_v1.handlers import traffic_map
from app.api.auth.jwt import auth_router


router = APIRouter()

router.include_router(user.user_router , prefix='/users' , tags=['users'])
router.include_router(traffic_map.traffic_map_router , prefix='/traffic_map' , tags=['users'])
router.include_router(auth_router , prefix='/auth' , tags=['auth'])


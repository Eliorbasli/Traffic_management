from fastapi import APIRouter
from app.api.api_v1.handlers import user
from app.api.api_v1.handlers import graph
from app.api.api_v1.handlers import car
from app.api.auth.jwt import auth_router


router = APIRouter()

router.include_router(user.user_router , prefix='/users' , tags=['users'])
router.include_router(graph.graph_router , prefix='/graph' , tags=['users'])
router.include_router(auth_router , prefix='/auth' , tags=['auth'])
router.include_router(car.car_router , prefix='/cars' , tags=['cars'])


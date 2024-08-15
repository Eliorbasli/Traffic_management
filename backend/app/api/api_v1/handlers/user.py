from fastapi import APIRouter, HTTPException , status
from app.schemas.user_schema import UserAuth
from app.services.user_service import userService

import pymongo
user_router = APIRouter()

@user_router.post('/create' , summary= " Create new user")
async def create_user(data: UserAuth):
    try:
        return await userService.creaate_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            details="User with this email or username already exist"
        )
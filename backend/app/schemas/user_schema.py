from pydantic import BaseModel , EmailStr , Field

class UserAuth(BaseModel):
    username: str = Field(... , min_length=5 , max_length=50 , description="user username")
    password: str = Field(... , min_length=5, max_length=24 , description="user password")
    email: EmailStr = Field( ... , description="user email")
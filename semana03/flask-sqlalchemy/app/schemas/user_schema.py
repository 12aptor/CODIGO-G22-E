from pydantic import BaseModel, EmailStr

class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr

class UserResponseSchema(UserCreateSchema):
    id: int
    created_at: str
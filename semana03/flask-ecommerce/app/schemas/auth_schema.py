from pydantic import BaseModel

class RegisterSchema(BaseModel):
    name: str
    last_name: str
    email: str
    password: str
    role_id: int

class UserSchema(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    status: bool
    created_at: str
    updated_at: str
    role_id: int
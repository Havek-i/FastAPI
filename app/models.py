from pydantic import BaseModel, EmailStr, PositiveInt, Field

# Типы данных
class SNum(BaseModel):
    num1: int
    num2: int

class User(BaseModel):
    id: int
    name: str

class Feedback(BaseModel):
    name: str
    message: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt | None = Field(default=None, lt=130)
    is_subscribed: bool | None = None
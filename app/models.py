from pydantic import BaseModel

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
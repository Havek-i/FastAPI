from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Annotated
import uvicorn

# Константы
PATH = 'app/templates'


# Движок
app = FastAPI()


# Типы данных
class SNum(BaseModel):
    num1: int
    num2: int


# Маршруты
@app.get("/")
async def root():
    return FileResponse(f'{PATH}/index.html')

@app.get("/calculate")
async def calculate():
    return FileResponse(f"{PATH}/calculate.html")

@app.post("/calculate")
async def calculate_post(data: Annotated[SNum, Form()]):
    return {"result": data.num1 + data.num2}


# Запуск файла
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )

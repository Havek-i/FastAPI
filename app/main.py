from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from typing import Annotated
from models import SNum, User
import uvicorn

# Константы
PATH = 'app/templates'


# Движок
app = FastAPI()

data = {
    'id': 1,
    'name': 'John Doe'
}

user = User(**data)

# Маршруты
@app.get("/")
async def root():
    return FileResponse(f'{PATH}/index.html')

@app.get("/calculate")
async def calculate():
    return FileResponse(f"{PATH}/calculate.html")

@app.get('/users')
async def get_user():
    return user


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

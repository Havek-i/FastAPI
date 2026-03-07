from fastapi import FastAPI, Form, Body, Path
from fastapi.responses import FileResponse
from typing import Annotated
from models import SNum, User, Feedback, UserCreate
import uvicorn

from db.db import sample_products

# Константы
PATH = 'app/templates'


# Движок
app = FastAPI()


# Маршруты
@app.get('/product/{product_id}')
def get_product(product_id: int):
    product = [item for item in sample_products if item['product_id'] == product_id]
    return product[0]

@app.get('/products/search')
def serach_products(keyword: str, category: str | None = None, limit: int = 10):
    result = list(filter(lambda item: keyword.lower() in item['name'].lower(), sample_products))

    if category:
        result = list(filter(lambda item: item["category"] == category, result))

    return result[:limit]


# Запуск файла
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()
app.counter = 0


@app.get("/items/{name}")
async def read_item(name: str):
    return {"Hello "+name}

@app.get("/counter")
def counter():
    app.counter += 1
    return str(app.counter)

class Product(BaseModel):
    name : str
    description: Union[str, None] = None
    price : float
    code : str
    tax : Union[float,None] = None

@app.post("/product")
def show_product(product: Product):
    return product


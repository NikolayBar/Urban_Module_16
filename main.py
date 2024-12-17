from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float


app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello FastAPI"}


# @app.get("/main")
# async def welcome() -> dict:
#     return {"message": "Main page"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {'item_id': item_id}


@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id,
            "name": item.name,
            "price": item.price}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}

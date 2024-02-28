"""
para commit mas rapidos, Ctrl + S x2, 
#Query parameters modificado haciendo pasos
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(start: int = 0, end: int = 10, skip: int = 0):
    return fake_items_db[start : start + end: skip]
"""
"""#query parameters"""
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
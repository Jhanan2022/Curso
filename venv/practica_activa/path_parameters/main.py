"""
#Parametros de ruta dinamicos
from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{item_id}')
async def read_item(item_id):
    return {'item_id':item_id}
"""
"""#parametros de ruta con tipos
from fastapi import FastAPI

app = FastAPI()

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return {'item_id':item_id}
"""
"""#El orden importa
from fastapi import FastAPI

app = FastAPI()

@app.get('/users/me')
async def read_user_me():
    return{"user_id":"the current user"}

@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return{"user_id": user_id}
"""
""" #Parametros de ruta enumerados
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
"""
"""#Parametro de ruta con una ruta en el parametro
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
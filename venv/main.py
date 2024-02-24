# Permitir la ejecucion de scripts: Set-ExecutionPolicy RemoteSigned -Scope Process
# correr la app uvicorn main:app --reload --port 5000
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hola':'Mundo'}

@app.get('/hola')
def hola_mundo():
    return {'Hola':'Mundo! 2'}

@app.get('/items/{item_id}')
def read_id(item_id: int, q: Union[str,None]=None):
    return {'item_id': item_id, 'q':q}

@app.get('/calculadora')
def calcular(operando1:float,operando2:float):
    return {'suma': operando1+operando2}
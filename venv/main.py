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
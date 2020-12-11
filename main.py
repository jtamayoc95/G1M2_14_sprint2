from db.user_db import UserInDB
from db.user_db import get_user, update_user

from models.user_models import UserIn, UserOut

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

import requests

# instanciate a fast object using the FastAPI class
app = FastAPI()

@app.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code = 404, detail = "El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@app.get("/user/data/{username}")
async def get_user_data(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code = 404, detail = "El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@app.put("/user/changepass/")
async def change_password(user_in: UserIn, new_password: str):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code = 404, detail = "El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Contraseña equivocada": False}
    user_in_db.password = new_password
    update_user(user_in_db)
    return {"Cambio de contraseña exitoso": True}

"""
@app.get('/cities')
def get_cities():
    results = []
    for city in db:
        r = requests.get(f'')
    return db

@app.get('/cities/{city_id}')
def get_city(city_id: int):
    return db[city_id-1]



@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}
"""
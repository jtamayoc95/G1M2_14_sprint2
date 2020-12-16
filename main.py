from db.user_db import UserInDB
from db.user_db import get_user, update_user

from models.user_models import UserIn, UserOut, NewPassword

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

import requests

# instanciate a fast object using the FastAPI class
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost.tiangolo.com", 
            "https://localhost.tiangolo.com",
            "http://localhost", 
            "http://localhost:8080",
            ]

app.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@app.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code = 404, detail = "El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Autenticado": False}
    return {"Autenticado": True}

@app.get("/user/data/{username}")
async def get_user_data(username):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code = 404, detail = "El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@app.put("/user/changepass/")
async def change_password(user_in: UserIn, new_password: NewPassword):
    user_in_db = get_user(user_in.username)
    if user_in_db == None:
        raise HTTPException(status_code = 404, detail = "El usuario no existe")
    if user_in_db.password != user_in.password:
        return {"Contraseña equivocada": True}
    user_in_db.password = new_password.new_password
    return {"Cambio de contraseña exitoso": True}

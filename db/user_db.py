from typing import Dict
from pydantic import BaseModel

class UserInDB(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    phone: int
    password: str

db_users = Dict[str, UserInDB]

db_users = {
    "jata": UserInDB(**{"username": "jata",
                        "first_name": "Jaime",
                        "last_name": "Tamayo",
                        "email": "jaimetamayo@yahoo.es",
                        "phone": 3017775010,
                        "password": "jaime123",
                        }),
    "magu": UserInDB(**{"username": "magu",
                        "first_name": "Martin",
                        "last_name": "Gutierrez",
                        "email": "martingutierrez@misena.edu.co",
                        "phone": 3124613216,
                        "password": "martin123",
                        }),
    "daca": UserInDB(**{"username": "daca",
                        "first_name": "Dayanna",
                        "last_name": "Campos",
                        "email": "dlcampos77@hotmail.com",
                        "phone": 3186205819,
                        "password": "dayanna123",
                    }),
    "cabe": UserInDB(**{"username": "cabe",
                        "first_name": "Camilo",
                        "last_name": "Bedoya",
                        "email": "tripitrue@hotmail.com",
                        "phone": 3003562551,
                        "password": "camilo123",
                        }),
    "joju": UserInDB(**{"username": "joju",
                        "first_name": "John",
                        "last_name": "Juez",
                        "email": "johnjuez@outlook.es",
                        "phone": 3127946214,
                        "password": "jhon123",
                        }),                                                                                    

}

def get_user(username: str):
    if username in db_users.keys():
        return db_users[username]
    else:
        return None

def update_user(user_in_db: UserInDB):
    db_users[user_in_db.username] = user_in_db
    return user_in_db

""" https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary
def delete_user(str, email):
    r = dict(d)
    del r[email]
    return r
"""

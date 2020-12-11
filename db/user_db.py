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
                        "email": "jtamayoc95@gmail.com",
                        "phone": 301794501,
                        "password": "jaime123",
                        }),
    "magu": UserInDB(**{"username": "magu",
                        "first_name": "Martin",
                        "last_name": "Gutierrez",
                        "email": "martin72.gutierrez@gmail.com",
                        "phone": 312777329,
                        "password": "martin123",
                        }),
    "daca": UserInDB(**{"username": "daca",
                        "first_name": "Dayanna",
                        "last_name": "Campos",
                        "email": "dlcampos77@misena.edu.co",
                        "phone": 318356518,
                        "password": "dayanna123",
                    }),
    "cabe": UserInDB(**{"username": "cabe",
                        "first_name": "Camilo",
                        "last_name": "Bedoya",
                        "email": "tipitreue@gmail.com",
                        "phone": 300620293,
                        "password": "camilo123",
                        }),
    "joju": UserInDB(**{"username": "joju",
                        "first_name": "Jhon",
                        "last_name": "Juez",
                        "email": "j0hnjuez@gmail.com",
                        "phone": 312461685,
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

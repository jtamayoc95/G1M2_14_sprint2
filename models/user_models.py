from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    phone: int

class NewPassword(BaseModel):
    new_password: str
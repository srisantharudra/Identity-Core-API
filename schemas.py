from sqlmodel import SQLModel
class UserCreate(SQLModel):
    username:str
    email:str
    role:str
    password:str
class UserRead(SQLModel):
    id:int
    username:str
    email:str
    role:str
class Userlogin(SQLModel):
    username:str
    role:str
    password:str
class jwt(SQLModel):
    access_token:str
    refresh_token:str
    token_type:str



    
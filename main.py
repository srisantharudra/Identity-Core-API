from fastapi import FastAPI
from sqlmodel import SQLModel
from database import engine
from routers import router
from models import User
app=FastAPI()
@app.on_event("startup")
def start():
    SQLModel.metadata.create_all(engine)
app.include_router(router) 




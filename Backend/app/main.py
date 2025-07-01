# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "API Python funcionando 🚀"}

# backend/app/main.py
from fastapi import FastAPI
from app.core.database import engine, Base
from app.Controllers import login_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Control Easy API")

app.include_router(login_controller.router)
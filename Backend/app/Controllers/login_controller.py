# Backend/app/Controllers/login_controller.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.login_schema import LoginRequest, LoginResponse
from app.services.auth_service import verificar_credenciais
from app.core.database import get_db

router = APIRouter(prefix="/login", tags=["Login"])

@router.post("/", response_model=LoginResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    return verificar_credenciais(db, login_data)

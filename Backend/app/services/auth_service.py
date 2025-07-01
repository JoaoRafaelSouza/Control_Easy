# backend/app/services/auth_service.py
from sqlalchemy.orm import Session
from app.models.usuario_model import Usuario
from app.schemas.login_schema import LoginRequest
from fastapi import HTTPException
from hashlib import sha256

def verificar_credenciais(db: Session, login_data: LoginRequest):
    usuario = db.query(Usuario).filter(Usuario.email == login_data.email).first()
    
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")

    senha_hash = sha256(login_data.password.encode()).hexdigest()

    if usuario.password != senha_hash:
        raise HTTPException(status_code=401, detail="Senha incorreta")

    # Gera token falso para exemplo, substitua por JWT depois
    return {"access_token": f"fake-token-{usuario.id}", "token_type": "bearer"}

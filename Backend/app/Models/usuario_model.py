# backend/app/models/usuario_model.py
from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    dtcreate = Column(DateTime, default=datetime.utcnow)
    dtbirth = Column(DateTime)
    phone1 = Column(String)
    phone2 = Column(String)
    nivelaccess = Column(String)
    password = Column(String)
    dtupdate = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

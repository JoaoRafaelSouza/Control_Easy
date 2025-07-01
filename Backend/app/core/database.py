# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os

# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres@db:5432/control_easy")

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False, autoFlush=False)

# backend/app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ajuste para seu banco:
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:suasenha@db:5432/controleasy"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
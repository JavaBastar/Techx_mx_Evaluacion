from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./chatbot.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

class Comprador(Base):
    __tablename__ = "compradores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    total_compras = Column(Float)

class Deudor(Base):
    __tablename__ = "deudores"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    monto_adeudado = Column(Float)

def crear_tablas():
    Base.metadata.create_all(bind=engine)

# app/main.py

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.nlp import detectar_intencion
from app.nlp_transformer import detectar_intencion_transformer
from app.chatbot import responder_a_intencion

app = FastAPI()

# Habilitar CORS para permitir conexión con el frontend en React (CRA usa puerto 3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de entrada
class Pregunta(BaseModel):
    texto: str

# Dependencia para obtener sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint con lógica de reglas
@app.post("/chatbot")
def chatbot(pregunta: Pregunta, db: Session = Depends(get_db)):
    intencion = detectar_intencion(pregunta.texto)
    respuesta = responder_a_intencion(intencion, db)
    return {"respuesta": respuesta}

# Endpoint con lógica usando transformers
@app.post("/chatbot-transformer")
def chatbot_transformer(pregunta: Pregunta, db: Session = Depends(get_db)):
    intencion = detectar_intencion_transformer(pregunta.texto)
    respuesta = responder_a_intencion(intencion, db)
    return {
        "respuesta": respuesta,
        "intencion_detectada": intencion
    }

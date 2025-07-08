# app/chatbot.py

from sqlalchemy.orm import Session
from app.database import Comprador, Deudor

def responder_a_intencion(intencion: str, db: Session) -> str:
    if intencion == "mejores_compradores":
        compradores = db.query(Comprador).order_by(Comprador.total_compras.desc()).limit(3).all()
        if not compradores:
            return "No hay compradores registrados."
        nombres = ", ".join(c.nombre for c in compradores)
        return f"Los mejores compradores son: {nombres}."

    elif intencion == "mayores_deudores":
        deudores = db.query(Deudor).order_by(Deudor.monto_adeudado.desc()).limit(3).all()
        if not deudores:
            return "No hay deudores registrados."
        nombres = ", ".join(d.nombre for d in deudores)
        return f"Los deudores con mayor deuda son: {nombres}."

    elif intencion == "contar_compradores":
        cantidad = db.query(Comprador).count()
        return f"Hay un total de {cantidad} compradores registrados."

    else:
        return "Lo siento, no entendí tu pregunta. ¿Podrías reformularla?"

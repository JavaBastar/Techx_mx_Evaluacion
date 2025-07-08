# app/nlp.py

def detectar_intencion(pregunta: str) -> str:
    pregunta = pregunta.lower()

    if "mejores compradores" in pregunta or "compran más" in pregunta:
        return "mejores_compradores"
    elif "deudores más altos" in pregunta or "mayores deudas" in pregunta or "debe más" in pregunta:
        return "mayores_deudores"
    elif "cuántos compradores" in pregunta or "número de compradores" in pregunta:
        return "contar_compradores"
    else:
        return "desconocido"

# app/nlp_transformer.py

from transformers import AutoTokenizer, AutoModel
import torch

# Cargar modelo multilingüe de Hugging Face
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-multilingual-cased")
model = AutoModel.from_pretrained("distilbert-base-multilingual-cased")

# Diccionario de intenciones y frases representativas
INTENTS = {
    "mejores_compradores": "quiénes son los mejores compradores",
    "mayores_deudores": "cuáles son los deudores más altos",
    "contar_compradores": "cuántos compradores hay",
}

# Función para obtener embedding promedio de una oración
def get_embedding(texto: str):
    inputs = tokenizer(texto, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze()

# Detección de intención mediante similitud de coseno
def detectar_intencion_transformer(pregunta: str) -> str:
    pregunta_emb = get_embedding(pregunta)

    similitudes = {}
    for clave, ejemplo in INTENTS.items():
        ejemplo_emb = get_embedding(ejemplo)
        cos_sim = torch.nn.functional.cosine_similarity(pregunta_emb, ejemplo_emb, dim=0)
        similitudes[clave] = cos_sim.item()

    mejor_intencion = max(similitudes, key=similitudes.get)
    return mejor_intencion if similitudes[mejor_intencion] > 0.5 else "desconocido"

# Ejercicio 3

Este proyecto es una aplicación web que permite comparar dos enfoques de chatbot para responder preguntas sobre una base de datos ficticia (compradores y deudores):

-  Basado en reglas (intents simples)
-  Basado en transformers (embeddings y similitud)

---

##  Estructura del proyecto

```
chatbot/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── chatbot.py
│   │   ├── nlp.py
│   │   └── nlp_transformer.py
│   ├── init_db.py
│   ├── chatbot.db
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── index.tsx
│   │   └── ...
│   └── package.json
```

---

##  Lógica del chatbot

- `chatbot.py`: lógica para consultar la base según la intención detectada.
- `nlp.py`: detección de intención con palabras clave.
- `nlp_transformer.py`: detección de intención con embeddings y similitud de coseno usando `distilbert-base-multilingual-cased`.

---

##  Backend (FastAPI + SQLite)

###  Requisitos

- Python 3.9+
- Crear entorno virtual:

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate       # En Windows
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Inicializar base de datos

```bash
python init_db.py
```

###  Ejecutar el backend

```bash
uvicorn app.main:app --reload
```

---

## Frontend (React + TypeScript)


###  Ejecutar frontend

```bash
npm start
```

Accede en: [http://localhost:3000]

---

## Endpoints del backend

- `POST /chatbot`  
  Devuelve respuesta basada en reglas.

- `POST /chatbot-transformer`  
  Devuelve respuesta basada en embeddings y similitud (Transformers).

---

## Preguntas que entiende

- ¿Quiénes son los mejores compradores?
- ¿Cuáles son los deudores más altos?
- ¿Cuántos compradores hay?



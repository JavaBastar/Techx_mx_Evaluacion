# Ejercicio 2

Este proyecto es una aplicación Full Stack construida con FastAPI (backend) y React + TypeScript (frontend). Permite hacer scraping de libros desde un sitio web y visualizar los datos almacenados en una tabla.

---

## Características

- Scraping desde cualquier URL (como books.toscrape.com)
- Guardado automático de datos en una base de datos SQLite
- Visualización de libros en frontend React
- Filtros por categoría y título
- Alerta flotante para errores o advertencias del scraping ⚠️

---

## Tecnologías utilizadas

### Backend
- Python 3.9+
- FastAPI
- SQLAlchemy
- BeautifulSoup
- SQLite

### Frontend
- React + TypeScript
- Axios

---

## Instalación

### 1. Backend (FastAPI)

```bash
cd backend
python -m venv env
.\env\Scripts\activate           # En Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

El backend correrá en: `http://localhost:8000`

### 2. Frontend (React)

```bash
cd ../frontend
npm install
npm start
```

El frontend correrá en: `http://localhost:3000`

---

## Endpoints API

### `POST /scrape`
Recibe una URL, hace scraping e intenta guardar los datos.

**Body JSON:**
```json
{
  "url": "http://books.toscrape.com/catalogue/page-1.html"
}
```

**Respuestas posibles:**
- `status: success` → datos guardados
- `status: warning` → no se encontraron productos en la página ⚠️
- `status: error` → no se pudo acceder a la URL ⚠️

---

### `GET /books`
Devuelve todos los libros almacenados. Permite filtros opcionales:

**Query params:**
- `category`: filtra por categoría (parcial, no sensible a mayúsculas)
- `title_contains`: filtra por coincidencias parciales en el título

**Ejemplos:**
```
/books?category=Horror
/books?title_contains=Python
```

---
## Base de datos

- El backend usa **SQLite** como base de datos local (`books.db`)
- Se configura con **SQLAlchemy** en el archivo `database.py`
- Las tablas se crean automáticamente al iniciar la aplicación

---

## Estructura del proyecto

```
proyecto-scraper/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── scraper.py
│   │   ├── models.py
│   │   └── database.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── api.ts
│   │   └── components/
│   │       └── BookTable.tsx
│   └── package.json
```

---

## Notas

- El backend incluye validación de errores para URLs incorrectas y páginas vacías.
- El frontend muestra mensajes flotantes según el tipo de respuesta (`success`, `warning`, `error`).
- Puedes usar cualquier página con estructura similar para pruebas, no se limita a books.toscrape.com.
- Se pueden tomar ejemplos de la siguiente página: http://books.toscrape.com/index.html

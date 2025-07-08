# Ejercicio 1

Este proyecto es una aplicación web full stack que permite **subir una imagen de un recibo**, procesarla con **OCR usando Tesseract**, y mostrar el texto extraído en pantalla. Está construido con **FastAPI en el backend** y **React + TypeScript en el frontend**.

---

## Tecnologías utilizadas

-  Python 3 + FastAPI  
-  OCR con pytesseract y Pillow  
-  React + TypeScript (Create React App)  
-  Comunicación vía HTTP con CORS habilitado

---

##  Cómo ejecutar el proyecto

### 🔧 Requisitos previos

- Python 3.8+
- Node.js (v16+ recomendado)
- Tesseract OCR (ver más abajo)

---


###  1. Backend (FastAPI)

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate          # PowerShell
# o
venv\Scripts\activate.bat        # cmd

pip install -r requirements.txt
uvicorn main:app --reload
```

Esto levanta la API en:  
 `http://localhost:8000`

---

### 2. Frontend (React)

En otra terminal:

```bash
cd frontend
npm install
npm start
```

Esto abre el frontend en:  
 `http://localhost:3000`

---

## ⚠️ IMPORTANTE: Instalar Tesseract OCR

El backend requiere que **Tesseract esté instalado en el sistema** para realizar OCR.  

🔗 Descarga recomendada para Windows:  
https://github.com/UB-Mannheim/tesseract/wiki

Durante la instalación:
- Asegúrate de marcar  *"Add to PATH"*
- O, en su defecto, edita el archivo `config.py` y especifica manualmente la ruta de instalación:

```python
# config.py
TESSERACT_CMD = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
TESSDATA_PATH = r"C:/Program Files/Tesseract-OCR/tessdata"
```


## 📦 Estructura del proyecto

```
Task1/
├── README.md
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   └── venv/
├── frontend/
│   ├── src/
│   │   └── App.tsx
│   ├── public/
│   └── package.json
```

---



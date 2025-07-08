# Ejercicio 4

Este proyecto implementa un sistema completo para **reconocimiento de dígitos escritos a mano** usando una **red neuronal convolucional (CNN)** entrenada con PyTorch y expuesta como servicio web con FastAPI. También incluye una **interfaz gráfica** construida en React para probar el modelo subiendo imágenes tipo MNIST (28x28 píxeles, escala de grises).

---

##  Estructura del proyecto

```
imagenes_cnn/
├── backend/                # Entrenamiento y API FastAPI
│   ├── model/              # Modelo entrenado (.pth)
│   ├── training/           # Script de entrenamiento
│   ├── main.py             # API con /predict-image
│   ├── requirements.txt
│   └── env/                # Entorno virtual (opcional)
│
├── frontend/               # Interfaz en React + TypeScript
│   └── src/App.tsx
```

---

##  Requisitos

- Python 3.10+
- Node.js y npm
---

##  Backend: entrenamiento y API

### 1. Crear entorno virtual

```bash
cd imagenes_cnn/backend
python -m venv env
env\Scripts\activate  # Windows
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Entrenar el modelo

```bash
python training/train_cnn.py
```

Esto descargará el dataset MNIST y guardará el modelo entrenado como:

```
backend/model/cnn_mnist.pth
```

### 4. Ejecutar la API

```bash
uvicorn main:app --reload
```

La API estará disponible en:

- `http://localhost:8000` (mensaje de prueba)

---

##  Frontend: Interfaz React


```bash
npm run dev
```

La app estará en:

- `http://localhost:5173`

> Asegúrate de que el backend esté ejecutándose antes de hacer predicciones.

---

## Final

Se pueden subir imágenes tipo MNIST (28x28 en escala de grises, PNG) desde la interfaz para probar la clasificación en tiempo real, se añaden tres ejemplos  en la carpeta samples.


---

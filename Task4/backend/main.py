from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import base64
import io
import os

# === Arquitectura del modelo (igual al entrenamiento) ===
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.fc = nn.Sequential(
            nn.Flatten(),
            nn.Linear(64 * 7 * 7, 128),
            nn.ReLU(),
            nn.Linear(128, 10)
        )

    def forward(self, x):
        x = self.conv(x)
        x = self.fc(x)
        return x

# === Inicializar la app ===
app = FastAPI(title="CNN MNIST API")

# === Middleware CORS para permitir acceso desde el frontend ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Cargar modelo entrenado ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CNN().to(device)

model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "model", "cnn_mnist.pth"))
if not os.path.exists(model_path):
    raise RuntimeError(f"Modelo no encontrado en: {model_path}")

model.load_state_dict(torch.load(model_path, map_location=device))
model.eval()

# === Transformaciones de imagen ===
transform = transforms.Compose([
    transforms.Grayscale(),
    transforms.Resize((28, 28)),
    transforms.ToTensor()
])

# === Esquema de entrada ===
class ImageInput(BaseModel):
    image_base64: str

# === Endpoint raíz ===
@app.get("/")
def root():
    return {"message": "API CNN funcionando correctamente"}

# === Endpoint principal: predicción ===
@app.post("/predict-image")
def predict_image(data: ImageInput):
    try:
        # Decodificar imagen base64
        image_data = base64.b64decode(data.image_base64)
        image = Image.open(io.BytesIO(image_data)).convert("L")

        # Preprocesamiento
        tensor = transform(image).unsqueeze(0).to(device)  # [1, 1, 28, 28]

        # Predicción
        with torch.no_grad():
            output = model(tensor)
            prediction = torch.argmax(output, dim=1).item()

        return {"prediction": prediction}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al procesar la imagen: {str(e)}")

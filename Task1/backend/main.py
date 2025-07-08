from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import pytesseract
import io
import os
import config

pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
os.environ["TESSDATA_PREFIX"] = config.TESSDATA_PATH


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)


@app.post("/upload-ocr")
async def upload_ocr(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
        text = pytesseract.image_to_string(image, lang="eng").strip()

        if not text:
            raise HTTPException(status_code=400, detail="No se detectó texto en la imagen cargada")

        return {"text": text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar la imagen cargada: {e}")

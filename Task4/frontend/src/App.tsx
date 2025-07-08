import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [image, setImage] = useState<File | null>(null);
  const [preview, setPreview] = useState<string | null>(null);
  const [prediction, setPrediction] = useState<number | null>(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file));
    }
  };

  const handlePredict = async () => {
    if (!image) return;

    const reader = new FileReader();
    reader.onloadend = async () => {
      const base64 = (reader.result as string).split(',')[1]; // solo los datos
      setLoading(true);
      try {
        const response = await axios.post('http://localhost:8000/predict-image', {
          image_base64: base64,
        });
        setPrediction(response.data.prediction);
      } catch (error) {
        console.error(error);
        alert("Error al predecir la imagen.");
      } finally {
        setLoading(false);
      }
    };

    reader.readAsDataURL(image);
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>Clasificador de Dígitos (CNN + FastAPI)</h1>
      <input type="file" accept="image/png" onChange={handleImageChange} />
      {preview && (
        <div style={{ margin: '1rem 0' }}>
          <img src={preview} alt="preview" width={100} />
        </div>
      )}
      <button onClick={handlePredict} disabled={!image || loading}>
        {loading ? "Cargando..." : "Predecir"}
      </button>
      {prediction !== null && (
        <h2>Predicción: {prediction}</h2>
      )}
    </div>
  );
}

export default App;

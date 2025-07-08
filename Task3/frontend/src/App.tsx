// src/App.tsx
import React, { useState } from 'react';
import axios from 'axios';

const App: React.FC = () => {
  const [pregunta, setPregunta] = useState('');
  const [respuestaReglas, setRespuestaReglas] = useState('');
  const [respuestaTransformer, setRespuestaTransformer] = useState('');

  const hacerPregunta = async () => {
    try {
      const [resp1, resp2] = await Promise.all([
        axios.post('http://localhost:8000/chatbot', { texto: pregunta }),
        axios.post('http://localhost:8000/chatbot-transformer', { texto: pregunta }),
      ]);

      setRespuestaReglas(resp1.data.respuesta);
      setRespuestaTransformer(resp2.data.respuesta);
    } catch (err) {
      setRespuestaReglas('Error al consultar el chatbot.');
      setRespuestaTransformer('Error al consultar el transformer.');
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>🤖 Chatbot Comparativo</h1>

      <input
        type="text"
        value={pregunta}
        onChange={(e) => setPregunta(e.target.value)}
        placeholder="Escribe tu pregunta..."
        style={{ width: '100%', padding: '10px', marginBottom: '1rem' }}
      />

      <button onClick={hacerPregunta} style={{ padding: '10px 20px' }}>
        Preguntar
      </button>

      <div style={{ marginTop: '2rem' }}>
        <h3>🔸 Respuesta con Reglas:</h3>
        <p>{respuestaReglas}</p>
      </div>

      <div style={{ marginTop: '2rem' }}>
        <h3>🔹 Respuesta con Transformers:</h3>
        <p>{respuestaTransformer}</p>
      </div>
    </div>
  );
};

export default App;

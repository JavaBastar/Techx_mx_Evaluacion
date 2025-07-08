import React, { useState } from 'react';

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [text, setText] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selected = e.target.files?.[0] || null;
    setFile(selected);
    setText('');
    setError('');
  };

  const handleUpload = async () => {
    if (!file) return;

    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/upload-ocr', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || 'Se tiene un error desconocido');
      }

      setText(data.text);
      setError('');
    } catch (err: any) {
      setError(err.message);
      setText('');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '40px auto', fontFamily: 'Segoe UI, sans-serif' }}>
      <h1 style={{ textAlign: 'center' }}>Detección de texto en recibos utilizando OCR</h1>

      <div style={{ marginBottom: '20px', textAlign: 'center' }}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <br />
        <button
          onClick={handleUpload}
          disabled={!file || loading}
          style={{
            marginTop: '12px',
            padding: '10px 20px',
            backgroundColor: '#007BFF',
            border: 'none',
            borderRadius: '5px',
            color: '#fff',
            cursor: file ? 'pointer' : 'not-allowed',
            opacity: file && !loading ? 1 : 0.6,
          }}
        >
          {loading ? 'Procesando...' : 'Procesar imagen'}
        </button>
      </div>

      {text && (
        <div
          style={{
            backgroundColor: '#f6f8fa',
            border: '1px solid #d0d7de',
            borderRadius: '6px',
            padding: '16px',
            whiteSpace: 'pre-wrap',
          }}
        >
          <h3>Texto detectado:</h3>
          <p>{text}</p>
        </div>
      )}

      {error && (
        <div style={{ color: '#b00020', marginTop: '20px', textAlign: 'center' }}>
          <strong>Error:</strong> {error}
        </div>
      )}
    </div>
  );
}

export default App;

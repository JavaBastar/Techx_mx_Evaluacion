import React, { useEffect, useState } from "react";
import { getBooks, scrapeBooks } from "./api";
import BookTable from "./components/BookTable";

function App() {
  const [books, setBooks] = useState([]);
  const [url, setUrl] = useState("");
  const [category, setCategory] = useState("");
  const [title, setTitle] = useState("");
  const [message, setMessage] = useState("");
  const [messageType, setMessageType] = useState<"success" | "error" | "warning">("success");

  const fetchBooks = async (filters?: { category?: string; title?: string }) => {
    const data = await getBooks(filters);
    setBooks(data);
  };

  const handleScrape = async () => {
    if (!url) return;

    try {
      const response = await scrapeBooks(url);
      const data = response.data;

      if (data.status === "error") {
        setMessageType("error");
        setMessage(data.message);
      } else if (data.status === "warning") {
        setMessageType("warning");
        setMessage(data.message);
      } else if (data.status === "success") {
        setMessageType("success");
        setMessage(data.message);
        await fetchBooks();
      }
    } catch (error) {
      setMessageType("error");
      setMessage("Error desconocido. Verifica la URL.");
    }

    setTimeout(() => setMessage(""), 4000);
  };

  const handleFilter = () => {
    fetchBooks({ category, title });
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  const getBackgroundColor = () => {
    if (messageType === "success") return "#4caf50";
    if (messageType === "warning") return "#ff9800";
    return "#f44336"; // error
  };

  return (
    <div style={{ padding: "2rem", position: "relative" }}>
      <h1>Scraper de Libros</h1>

      {message && (
        <div
          style={{
            position: "fixed",
            top: "20px",
            right: "20px",
            padding: "1rem",
            backgroundColor: getBackgroundColor(),
            color: "#fff",
            borderRadius: "5px",
            boxShadow: "0px 0px 10px rgba(0,0,0,0.2)",
            zIndex: 1000,
          }}
        >
          {message}
        </div>
      )}

      <div style={{ marginBottom: "1rem" }}>
        <input
          type="text"
          value={url}
          placeholder="URL a scrapear"
          onChange={(e) => setUrl(e.target.value)}
          style={{ width: "300px", marginRight: "0.5rem" }}
        />
        <button onClick={handleScrape}>Scrapear</button>
      </div>

      <div style={{ marginBottom: "2rem" }}>
        <input
          type="text"
          value={title}
          placeholder="Filtrar por título"
          onChange={(e) => setTitle(e.target.value)}
          style={{ marginRight: "0.5rem" }}
        />
        <input
          type="text"
          value={category}
          placeholder="Filtrar por categoría"
          onChange={(e) => setCategory(e.target.value)}
          style={{ marginRight: "0.5rem" }}
        />
        <button onClick={handleFilter}>Filtrar</button>
      </div>

      <BookTable books={books} />
    </div>
  );
}

export default App;

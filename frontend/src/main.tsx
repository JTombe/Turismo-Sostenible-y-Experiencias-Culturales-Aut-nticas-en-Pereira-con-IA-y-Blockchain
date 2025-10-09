import React, { useState } from "react";
import ReactDOM from "react-dom/client";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:3000";

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch(`${API_URL}/generate?prompt=${encodeURIComponent(prompt)}`, {
      method: "POST",
    });
    const data = await res.json();
    setResponse(data.response || JSON.stringify(data));
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Cliente Ollama</h1>
      <form onSubmit={handleSubmit}>
        <textarea
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          className="border p-2 w-full"
        />
        <button className="bg-blue-500 text-white px-4 py-2 mt-2 rounded">
          Enviar
        </button>
      </form>
      <pre className="mt-4 whitespace-pre-wrap">{response}</pre>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")!).render(<App />);

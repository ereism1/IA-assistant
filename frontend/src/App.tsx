import { useState } from "react";
import { api } from "../services/api";
import { FaDatabase } from "react-icons/fa";


function App() {
  const [pergunta, setPergunta] = useState("");
  const [resposta, setResposta] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  async function consultar() {
    try {
      setLoading(true);

      const result = await api.post("/pergunta", {
        pergunta,
      });

      setResposta(result.data);
    } catch (error) {
      console.error(error);
      alert("Erro ao consultar API");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ padding: "40px" }}>
      <h1> <FaDatabase />Assistente SQL IA</h1>

      <input
        value={pergunta}
        onChange={(e) => setPergunta(e.target.value)}
        placeholder="Digite sua pergunta"
        style={{
          width: "400px",
          padding: "10px"
        }}
      />

      <button
        onClick={consultar}
        style={{
          marginLeft: "10px",
          padding: "10px"
        }}
      >
        Consultar
      </button>

      {loading && <p>Consultando...</p>}

{resposta && (
  <div
    style={{
      marginTop: "30px",
      padding: "20px",
      borderRadius: "12px",
      backgroundColor: "#1e293b"
    }}
  >
    <h2>Resposta</h2>

    <p
      style={{
        fontSize: "18px",
        lineHeight: "1.6"
      }}
    >
      {resposta.resposta}
    </p>
  </div>
)}
    </div>
  );
}

export default App;
import "./App.css";
import { useState } from "react";
import axios from "axios";

function App() {
  const [videoUrl, setVideoUrl] = useState("");
  const [transcript, setTranscript] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const getTranscript = async () => {
    try {
      let videoId = "";

      if (videoUrl.includes("v=")) {
        videoId = videoUrl.split("v=")[1].split("&")[0];
      } else if (videoUrl.includes("youtu.be/")) {
        videoId = videoUrl.split("youtu.be/")[1].split("?")[0];
      }

      const response = await axios.get(
        `http://127.0.0.1:8000/transcript/${videoId}`
      );

      setTranscript(response.data.transcript);
    } catch (error) {
      console.error(error);
      setTranscript("Failed to fetch transcript");
    }
  };

  const askQuestion = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/ask",
        {
          question: question,
        }
      );

      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
      setAnswer("Failed to get answer");
    }
  };

  return (
    <div className="container">

      <h1 className="title">⚡ UMATE</h1>

      <p className="subtitle">
        AI Powered YouTube Learning Assistant
      </p>

      <div className="card">
        <h2 className="section-title">🎥 YouTube Video</h2>

        <input
          className="input"
          type="text"
          placeholder="Paste YouTube URL Here..."
          value={videoUrl}
          onChange={(e) => setVideoUrl(e.target.value)}
        />

        <button
          className="button"
          onClick={getTranscript}
        >
          Get Transcript
        </button>
      </div>

      <div className="card">
        <h2 className="section-title">📜 Transcript</h2>

        <textarea
          className="textarea"
          value={transcript}
          readOnly
        />
      </div>

      <div className="card">
        <h2 className="section-title">❓ Ask Questions</h2>

        <input
          className="input"
          type="text"
          placeholder="Ask anything about this course..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button
          className="button"
          onClick={askQuestion}
        >
          Ask AI
        </button>
      </div>

      <div className="card">
        <h2 className="section-title">🤖 AI Answer</h2>

        <div className="answer-box">
          {answer}
        </div>
      </div>

      <div className="footer">
        Powered by UMATE • RAG + Gemini + ChromaDB
      </div>

    </div>
  );
}

export default App;
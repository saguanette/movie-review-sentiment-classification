import React, { useState } from "react";
import "./App.css";

function App() {
  const [review, setReview] = useState("");
  const [sentiment, setSentiment] = useState("");
  const [model, setModel] = useState("lr");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await fetch(`http://127.0.0.1:8000/predict/${model}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ review }),
    });

    const data = await response.json();
    setSentiment(data.sentiment);
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundImage: "url(/background.jpg)",
        backgroundSize: "cover",
        backgroundPosition: "center",
        padding: "20px"
      }}>

    <div className= "app-container">
      <h2>🎬 Movie Review Sentiment Classifier</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          rows="5"
          cols="60"
          value={review}
          onChange={(e) => setReview(e.target.value)}
          placeholder="Type your movie review here..."
        />
      <br/>

        <label style={{ marginRight: "10px" }}>Choose Model:</label>
        <select value={model} onChange={(e) => setModel(e.target.value)}>
          <option value="lr">Logistic Regression</option>
          <option value="nb">Naive Bayes</option>
          <option value="svc">Support Vector Classifier</option>
        </select>

        <br />
        <button type="submit" style={{ marginTop: "10px" }}>Analyze</button>
      </form>
      
      {sentiment && (
        <h3>
          This review is <span>{sentiment}</span>
        </h3>
      )}
    </div>
  </div>
  );
}

export default App;

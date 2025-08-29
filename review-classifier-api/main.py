from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware
from schemas import ReviewRequest
from models import predict_sentiment, model_nb, model_lr, model_svc


app = FastAPI(title="Movie Review Sentiment Classifier")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Title": "Movie Review Sentiment Classifier"}

@app.post("/predict/{model_name}")
def predict(model_name: str, req: ReviewRequest):
    models = {"lr": model_lr, "nb": model_nb, "svc": model_svc}
    if model_name not in models:
        return {"error": "Model not found"}
    sentiment = predict_sentiment(models[model_name], req.review)
    return {"review": req.review, "sentiment": sentiment, "model": model_name.upper()}



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # use Render's port or 8000 locally
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)


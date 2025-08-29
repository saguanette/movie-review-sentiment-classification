from preprocessing import preprocessing_pipeline
import joblib 
from fastapi import HTTPException


vectorizer = joblib.load("models/vectorizer.pkl")
model_lr = joblib.load("models/lr.pkl")
model_nb = joblib.load("models/nb.pkl")
model_svc = joblib.load("models/svc.pkl")

MODELS = {
    "logistic regression": model_lr,
    "naive bayes": model_nb,
    "support vector classifier": model_svc
}


def predict_sentiment(model, review: str):
    try:
        review_cleaned = preprocessing_pipeline(review)
        review_transformed = vectorizer.transform([review_cleaned])
        pred = model.predict(review_transformed)[0]
        return "positive" if pred == 1 else "negative"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
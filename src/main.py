import joblib
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

from src.helper_pred import predict_top5

from fastapi import FastAPI
app = FastAPI()

# MODEL_SELECTED =  'logistic_regression'
MODEL_SELECTED =  'sgc_classifier'

def load_model():
    #print the current path
    import os
    print(os.getcwd())
    
    # Load model from disk
    model = joblib.load(f'models/model_{MODEL_SELECTED}.pkl')
    
    return model

def load_vectorizer():
    vectorizer = joblib.load(f'models/vectorizer_{MODEL_SELECTED}.pkl')
    return vectorizer

app.state.model = load_model()
app.state.vectorizer = load_vectorizer()

@app.get("/")
async def root():
    return {"message": "Welcome to the CCC Automation - Product Name Prediction API!"}


@app.get("/predict/{title}")
async def predict(title: str):
    title_cleaned, predictions = get_predictions(title)
    response = {"Title Cleaned": title_cleaned, "Product Name": predictions}
    return response

def get_predictions(title):
    df = predict_top5(model = app.state.model, vectorizer = app.state.vectorizer, X_test = [title])
    if df is None:
        return "None", "Cannot predict"
    else:
        predictions = df.iloc[0, 1:11].tolist()
        title = df.iloc[0, 0]
        return title, predictions


# main.py
import uvicorn
from fastapi import FastAPI
from Taap_accident import Taap_acc
import joblib
import numpy as np
import pandas as pd

# Load the model
model = joblib.load("t_accident_pred.joblib")

# Initialize app
taap_app = FastAPI()

# Home route
@taap_app.get("/")
def read_root():
    return {"message": "Model API is running!"}

# Prediction route
@taap_app.post("/predict")
def predict(data: Taap_acc):
    features = pd.DataFrame([{"Hour":data.Hour, "Day":data.Day, "LatBin":data.LatBin, "LonBin":data.LonBin}])
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
# if __name__ == '__main__':
#     uvicorn.run(taap_app, host='127.0.0.1', port=8000,reload=True)
# uvicorn taap_app:taap_app --reload

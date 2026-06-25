from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# ==========================================================
# Load Trained Machine Learning Pipeline
# ==========================================================

model = joblib.load("personality_classifier.pkl")

# ==========================================================
# Create FastAPI Application
# ==========================================================

app = FastAPI(
    title="Personality Prediction API",
    description="Predict whether a person is an Introvert or Extrovert",
    version="1.0"
)

# ==========================================================
# Input Schema
# ==========================================================

class PersonalityInput(BaseModel):
    Time_spent_Alone: int
    Stage_fear: str
    Social_event_attendance: int
    Going_outside: int
    Drained_after_socializing: str
    Friends_circle_size: int
    Post_frequency: int


# ==========================================================
# Home Endpoint
# ==========================================================

@app.get("/")
def home():
    return {
        "message": "Personality Prediction API is Running Successfully"
    }


# ==========================================================
# Prediction Endpoint
# ==========================================================

@app.post("/predict")
def predict(data: PersonalityInput):

    # Convert JSON to DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Make Prediction
    prediction = model.predict(input_data)[0]

    # Return Result
    return {
        "prediction": prediction
    }
# Introvert vs Extrovert Personality Prediction API

## Project Overview

This project is a Machine Learning-based REST API that predicts whether a person is an **Introvert** or an **Extrovert** based on their behavioral and social characteristics.

The project follows a complete machine learning workflow, including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, model serialization, API development, local testing, and cloud deployment.

The API is built using **FastAPI** and deployed on **Hugging Face Spaces**.

---

# Features

- Personality prediction using Machine Learning
- FastAPI REST API
- Interactive Swagger API documentation
- Cloud deployment on Hugging Face Spaces
- JSON request and response format
- Preprocessing integrated into the trained pipeline
- Public API endpoint

---

# Machine Learning Workflow

1. Dataset Understanding
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature Engineering
5. Model Development
6. Model Evaluation
7. Model Selection
8. Model Saving
9. API Development
10. Local API Testing
11. Cloud Deployment
12. API Verification

---

# Dataset Features

| Feature | Description |
|----------|-------------|
| Time_spent_Alone | Time spent alone |
| Stage_fear | Whether the person has stage fear |
| Social_event_attendance | Frequency of attending social events |
| Going_outside | Frequency of going outside |
| Drained_after_socializing | Whether the person feels drained after socializing |
| Friends_circle_size | Number of close friends |
| Post_frequency | Social media posting frequency |

### Target Variable

- Introvert
- Extrovert

---

# Technologies Used

- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- Uvicorn
- Hugging Face Spaces
- Git
- GitHub

---

# Project Structure

```
personality-prediction-api/
│
├── app.py
├── personality_classifier.pkl
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone https://huggingface.co/spaces/Gaminda123/personality-prediction-api
```

Move into the project

```bash
cd personality-prediction-api
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run the API

```bash
uvicorn app:app --reload
```

The API will start at

```
http://127.0.0.1:8000
```

Swagger documentation

```
http://127.0.0.1:8000/docs
```

---

# Public API

### Swagger Documentation

```
https://gaminda123-personality-prediction-api.hf.space/docs
```

### Prediction Endpoint

```
https://gaminda123-personality-prediction-api.hf.space/predict
```

---

# API Request

POST

```
/predict
```

Request Body

```json
{
  "Time_spent_Alone": 4,
  "Stage_fear": "No",
  "Social_event_attendance": 4,
  "Going_outside": 6,
  "Drained_after_socializing": "No",
  "Friends_circle_size": 13,
  "Post_frequency": 5
}
```

---

# API Response

```json
{
    "prediction":"Extrovert"
}
```

or

```json
{
    "prediction":"Introvert"
}
```

---

# Model Information

Problem Type

- Binary Classification

Machine Learning Framework

- Scikit-learn

Deployment Framework

- FastAPI

Model Serialization

- Joblib (.pkl)

---

# Evaluation Metrics

The trained models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

The best-performing model was selected and deployed.

---

# Local Testing

The API was tested using

- Swagger UI
- Postman
- FastAPI Interactive Documentation

---

# Deployment

The API is deployed on

- Hugging Face Spaces

Deployment Status

- Public
- Online
- Accessible through HTTPS

---

# Author

**Gaminda Premasiri**

AI/ML Engineer Intern

Faculty of Computing and Technology

University of Kelaniya

Sri Lanka

---

# License

This project was developed as part of a Machine Learning technical assessment and is intended for educational and evaluation purposes.

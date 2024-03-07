from fastapi import HTTPException
from joblib import load
from app.Model.diabetes_model import DiabetesFormData

# Cargar el modelo diabete.pkl
model = load("diabetes_model.pkl")

def predict_diabetes(data: DiabetesFormData):
    # Realizar la predicción
    features = [data.pregnancies, data.plasma_glucose, data.diastolic_blood_pressure, data.triceps_thickness,
                data.serum_insulin, data.bmi, data.diabetes_pedigree, data.age]
    prediction = model.predict([features])[0]
    
    return prediction

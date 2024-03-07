# Modelo para la presentacion de datos que requiere el modelo de diabetes
from pydantic import BaseModel

class DiabetesFormData(BaseModel):
    pregnancies: float
    plasma_glucose: float
    diastolic_blood_pressure: float
    triceps_thickness: float
    serum_insulin: float
    bmi: float
    diabetes_pedigree: float
    age: float
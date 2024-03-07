from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.Controller.diabetes_controller import predict_diabetes
from app.Model.diabetes_model import DiabetesFormData
app = FastAPI()
app.mount("/static", StaticFiles(directory="app/templates"), name="static")
# Ruta del formulario de datos
@app.get('/')
async def form():
    with open("app\View\dibetes_view.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content, status_code=200)

# se obtiene la prediccion en base a los datos enviados
@app.post('/predict')
async def predict(data: DiabetesFormData):
    prediction = predict_diabetes(data)
    result_message = "Tiene Diabetes" if prediction else "No tiene Diabetes"
    return HTMLResponse(content=f"<h1> {result_message}</h1>", status_code=200)


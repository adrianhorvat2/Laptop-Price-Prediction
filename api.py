import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Inicijalizacija FastAPI aplikacije
api = FastAPI()

# Učitavanje modela
with open("laptop_price_model.pkl", "rb") as f:
    model = pickle.load(f)

class LaptopFeatures(BaseModel):
    Brand: str
    Processor: str
    RAM_GB: int
    Storage: int
    GPU: str
    Screen_Size_inch: float
    Resolution: str
    Battery_Life_hours: float
    Weight_kg: float
    Operating_System: str

@api.post("/predict")
def predict(features: LaptopFeatures):

    df = pd.DataFrame([features.dict()])
    
    prediction = model.predict(df)
    
    return {"predicted_price": prediction[0]}

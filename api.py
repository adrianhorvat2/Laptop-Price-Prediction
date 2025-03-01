import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Učitavanje modela
with open("laptop_price_model.pkl", "rb") as f:
    model = pickle.load(f)

categorical_columns = ["Brand", "Processor", "Storage", "GPU", "Resolution", "Operating_System"]

class LaptopFeatures(BaseModel):
    Brand: str
    Processor: str
    RAM_GB: int
    Storage: str  
    GPU: str
    Screen_Size_inch: float
    Resolution: str  
    Battery_Life_hours: float
    Weight_kg: float
    Operating_System: str

@app.post("/predict")
def predict(features: LaptopFeatures):
  
    df = pd.DataFrame([features.dict()])
    
    df = pd.get_dummies(df, columns=categorical_columns)

    model_columns = model.feature_names_in_
    missing_cols = [col for col in model_columns if col not in df.columns]
    for col in missing_cols:
        df[col] = 0

    df = df[model_columns]
    
    prediction = model.predict(df)

    return {"predicted_price": float(prediction[0])}
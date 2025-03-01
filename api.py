import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import MinMaxScaler

app = FastAPI()

with open("laptop_price_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

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

    df = df.reindex(columns=model_columns, fill_value=0)

    numeric_features = ["RAM_GB", "Screen_Size_inch", "Battery_Life_hours", "Weight_kg"]
    df[numeric_features] = scaler.transform(df[numeric_features])  

    prediction = model.predict(df)

    return {"predicted_price": float(prediction[0])}
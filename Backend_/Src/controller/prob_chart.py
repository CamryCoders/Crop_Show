from fastapi import APIRouter
from pydantic import BaseModel, Field
import numpy as np

from load_data import label_encoder, model, scaler

router = APIRouter(prefix="/api/crop", tags=["Crop"])

class CropInput(BaseModel):
    N: float = Field(..., ge=0)
    P: float = Field(..., ge=0)
    K: float = Field(..., ge=0)
    temperature: float = Field(..., ge=-50, le=60)
    humidity: float = Field(..., ge=0, le=100)
    ph: float = Field(..., ge=0, le=14)
    rainfall: float = Field(..., ge=0)

@router.post("/chart")
def show_prediction_chart(data: CropInput):
    input_data = np.array([[
        data.N,
        data.P,
        data.K,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall,
    ]])
    
    # 1. Scale the input data
    input_scaled = scaler.transform(input_data)
    
    # 2. Run inference using ONNX Runtime (replaces model.predict)
    input_tensor = input_scaled.astype(np.float32)
    input_name = model.get_inputs()[0].name
    
    outputs = model.run(None, {input_name: input_tensor})
    probabilities = outputs[0][0]  # Extracts probability distribution array
    
    # 3. Build response payload
    probability_data = []
    for crop, probability in zip(label_encoder.classes_, probabilities):
        probability_data.append({
            "crop": crop,
            "probability": round(float(probability * 100), 2),
        })
        
    return probability_data
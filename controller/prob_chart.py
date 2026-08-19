from pathlib import Path
import numpy as np
import joblib
from flask import request
import tensorflow as tf
from load_data import model,scaler,label_encoder




def show_prediction_chart(
   
):
    data=request.get_json()

    input_data=np.array([
            [data.get("N"),
             data.get("P"),
             data.get("K"),
             data.get("temperature"),
             data.get("humidity"),
             data.get("ph"),
             data.get("rainfall"),]
        ])

    input_scaled = scaler.transform(input_data)

    probabilities = model.predict(input_scaled, verbose=0)[0]

    top_indices = np.argsort(probabilities)[-5:][::-1]

    crops = label_encoder.inverse_transform(top_indices)

    scores = probabilities[top_indices] * 100
    probability_data = []

    for crop, probability in zip(
        label_encoder.classes_,
        probabilities
    ):
    
        probability_data.append({
            "crop": crop,
            "probability": round(
                float(probability * 100),
                2
            )
        })
    return probability_data

    
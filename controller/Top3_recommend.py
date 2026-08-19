from pathlib import Path
import numpy as np

import tensorflow as tf
from flask import request
from load_data import model,scaler,label_encoder


def top_3_crops():
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

    top_3_indices = np.argsort(probabilities)[-3:][::-1]

    top_3_crop=[]

    print("Top 3 Recommended Crops:\n")

    for index in top_3_indices:

        crop = label_encoder.inverse_transform([index])[0]

        confidence = probabilities[index] * 100

        top_3_crop.append({
            "crop":crop,
            "probability": round(float(confidence),2)
        })
        return top_3_crop

        
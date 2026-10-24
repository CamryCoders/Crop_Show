from pathlib import Path
import joblib
import onnxruntime as ort
import numpy as np
import time

start = time.time()
BASE_DIR = Path(__file__).resolve().parent.parent
print("Base_dir", BASE_DIR)

# Point to your ONNX model instead of the .keras file
MODEL_PATH = BASE_DIR / "models" / "crop_model.onnx"

print("Path:", MODEL_PATH)
print("Exists:", MODEL_PATH.exists())
print("Size:", MODEL_PATH.stat().st_size, "bytes")

# Load the ONNX inference session (lightweight and fast)
model = ort.InferenceSession(str(MODEL_PATH))
print("After loading ONNX model:", time.time() - start)

scaler = joblib.load(
    BASE_DIR / "models" / "scaler.pkl"
)
print("After loading scaler:", time.time() - start)

label_encoder = joblib.load(
    BASE_DIR / "models" / "label_encoder.pkl"
)
print("Finished loading all artifacts:", time.time() - start)
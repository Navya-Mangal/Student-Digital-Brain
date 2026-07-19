import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "ml", "student_recommendation.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "ml", "feature_encoders.pkl")
TARGET_PATH = os.path.join(BASE_DIR, "ml", "target_encoder.pkl")


with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(ENCODER_PATH, "rb") as f:
    feature_encoders = pickle.load(f)

with open(TARGET_PATH, "rb") as f:
    target_encoder = pickle.load(f)
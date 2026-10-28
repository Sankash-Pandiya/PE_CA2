import os
from functools import lru_cache
from pathlib import Path

import joblib

DEFAULT_MODEL_PATH = Path(__file__).resolve().parents[1] / "house_price_model.pkl"


@lru_cache(maxsize=1)
def load_model():
    model_path = Path(os.environ.get("MODEL_PATH", DEFAULT_MODEL_PATH))
    if not model_path.is_file():
        raise FileNotFoundError(f"Model file does not exist: {model_path}")
    return joblib.load(model_path)

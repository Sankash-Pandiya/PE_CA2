import logging

from fastapi import FastAPI, HTTPException
import pandas as pd

from house_price_api.predictor import load_model
from house_price_api.schemas import HouseFeatures, PredictionResponse

logger = logging.getLogger(__name__)

MODEL_FEATURES = (
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "condition",
)

app = FastAPI(
    title="House Price Prediction API",
    description="Predict house prices from selected property features.",
    version="1.0.0",
)


@app.get("/", tags=["health"])
def read_root():
    return {
        "message": "Welcome to the House Price Prediction API. "
        "Use the /predict endpoint."
    }


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}


@app.post(
    "/predict",
    response_model=PredictionResponse,
    tags=["predictions"],
)
def predict_price(features: HouseFeatures) -> PredictionResponse:
    input_data = pd.DataFrame(
        [features.model_dump()],
        columns=MODEL_FEATURES,
    )

    try:
        model = load_model()
    except FileNotFoundError as error:
        logger.error("House price model artifact is unavailable: %s", error)
        raise HTTPException(
            status_code=503,
            detail="The prediction model is unavailable.",
        ) from error

    prediction = model.predict(input_data)[0]
    return PredictionResponse(predicted_price=float(prediction))

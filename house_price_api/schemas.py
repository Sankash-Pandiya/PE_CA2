from pydantic import BaseModel


class HouseFeatures(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: int
    sqft_lot: int
    floors: float
    condition: int


class PredictionResponse(BaseModel):
    predicted_price: float

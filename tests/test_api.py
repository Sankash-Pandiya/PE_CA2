from fastapi.testclient import TestClient

from house_price_api.main import app

client = TestClient(app)

HOUSE_FEATURES = {
    "bedrooms": 3,
    "bathrooms": 2.5,
    "sqft_living": 1710,
    "sqft_lot": 8560,
    "floors": 2.0,
    "condition": 4,
}


def test_root_and_health_endpoints():
    root_response = client.get("/")
    health_response = client.get("/health")

    assert root_response.status_code == 200
    assert "House Price Prediction API" in root_response.json()["message"]
    assert health_response.status_code == 200
    assert health_response.json() == {"status": "ok"}


def test_predict_returns_a_price():
    response = client.post("/predict", json=HOUSE_FEATURES)

    assert response.status_code == 200
    assert isinstance(response.json()["predicted_price"], float)
    assert response.json()["predicted_price"] > 0


def test_predict_rejects_missing_features():
    response = client.post("/predict", json={"bedrooms": 3})

    assert response.status_code == 422

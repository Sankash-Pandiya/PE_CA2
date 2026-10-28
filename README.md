# House Price Prediction API

A FastAPI service that uses the included `house_price_model.pkl` artifact to
predict house prices.

## Project structure

```text
PE_CA2/
├── .github/
│   └── workflows/
│       └── ci.yml
├── house_price_api/
│   ├── __init__.py
│   ├── main.py
│   ├── predictor.py
│   └── schemas.py
├── tests/
│   └── test_api.py
├── app.py
├── house_price_model.pkl
├── requirements-dev.txt
└── requirements.txt
```

## Run locally

Use Python 3.11, create and activate a virtual environment, then install the
dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
```

Start the API from the project directory:

```powershell
python -m uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.
The API also exposes `GET /health` and `POST /predict`.

Example request:

```json
{
  "bedrooms": 3,
  "bathrooms": 2.5,
  "sqft_living": 1710,
  "sqft_lot": 8560,
  "floors": 2.0,
  "condition": 4
}
```

The model file is loaded from the project directory by default. To use a
different artifact, set the `MODEL_PATH` environment variable to its path.
The included model was serialized with scikit-learn 1.6.1, so that version is
pinned in `requirements.txt` to keep loading compatible.

## Test

```powershell
python -m pytest
```

GitHub Actions runs the test suite on pushes and pull requests targeting
`main` or `master`.

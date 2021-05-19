import os
import pytest

import pandas as pd
from fastapi.testclient import TestClient

from app import app


@pytest.fixture()
def dataset_path() -> str:
    return "data/raw/heart.csv"


@pytest.fixture()
def model_path() -> str:
    os.environ['PATH_TO_MODEL'] = 'models/model.pkl'
    return os.getenv("PATH_TO_MODEL")


def test_get_main(model_path):
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == "Entry point of our predictor"


def test_get_predict(dataset_path, model_path):
    with TestClient(app) as client:
        data = pd.read_csv(dataset_path)
        data["id"] = data.index + 1
        features = data.columns.tolist()
        data = data.values.tolist()[:5]
        response = client.get("/predict/", json={"data": data, "features": features})
        assert response.status_code == 200
        assert response.json()[0]["disease"] == 1


def test_invalid_prediction(model_path):
    with TestClient(app) as client:
        random_data = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
        features = random_data.columns.tolist()
        random_data = random_data.values.tolist()
        response = client.get("/predict/", json={"data": random_data, "features": features})
        assert response.status_code != 200

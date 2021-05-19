import os
import logging
from typing import List, Optional

import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
from sklearn.pipeline import Pipeline

from src.entities import HeartDiseaseModel, DiseaseResponse
from src.model_routines import load_model_from_path


logger = logging.getLogger(__name__)

model: Optional[Pipeline] = None


def make_predict(
    data: List,
    features: List[str],
    model: Pipeline,
) -> List[DiseaseResponse]:
    try:
        data = pd.DataFrame(data, columns=features)
        ids = [int(x) for x in data["id"]]
        data.drop(columns=["id"], inplace=True)
        if "target" in features:
            data.drop(columns=["target"], inplace=True)
        prediction = model.predict(data)

        return [
            DiseaseResponse(id=id_, disease=disease) for id_, disease in zip(ids, prediction)
        ]

    except Exception as e:
        raise HTTPException(status_code=400)


app = FastAPI()


@app.get("/")
def main():
    return "Entry point of our predictor"


@app.on_event("startup")
def load_model():
    global model
    model_path = os.getenv("PATH_TO_MODEL")
    if model_path is None:
        err = f"PATH_TO_MODEL {model_path} is None"
        logger.error(err)
        raise RuntimeError(err)
    model = load_model_from_path(model_path)


@app.get("/health")
def health() -> bool:
    return not (model is None)


@app.get("/predict/", response_model=List[DiseaseResponse])
def predict(request: HeartDiseaseModel):
    return make_predict(request.data, request.features, model)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))

import os
import time
import logging
from typing import List, Optional

import uvicorn
from fastapi import FastAPI, HTTPException
from sklearn.pipeline import Pipeline

from src.entities import HeartDiseaseModel, DiseaseResponse
from src.model_routines import load_model_from_path
from src.data_validation import prepare_and_validate_data


logger = logging.getLogger(__name__)

model: Optional[Pipeline] = None


def make_predict(
    request: HeartDiseaseModel,
) -> List[DiseaseResponse]:
    global model
    try:
        ids, data = prepare_and_validate_data(request)
        prediction = model.predict(data)
        return [
            DiseaseResponse(id=id_, disease=disease) for id_, disease in zip(ids, prediction)
        ]
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=400)


app = FastAPI()

start_time = time.time()
APP_START_DELAY = 30
APP_DURATION = 100


@app.get("/")
def main():
    return "Heart Disease prediction model"


@app.on_event("startup")
def load_model():
    global model
    time.sleep(APP_START_DELAY)
    model_path = os.getenv("PATH_TO_MODEL")
    if model_path is None:
        err = f"PATH_TO_MODEL {model_path} is None"
        logger.error(err)
        raise RuntimeError(err)
    model = load_model_from_path(model_path)


@app.get("/status")
def health() -> bool:
    if time.time() - start_time > APP_DURATION:
        raise RuntimeError("Application runtime limit exceeded.")
    return not (model is None)


@app.post("/predict/", response_model=List[DiseaseResponse])
def predict(request: HeartDiseaseModel):
    global model
    return make_predict(request)


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=os.getenv("PORT", 8000))

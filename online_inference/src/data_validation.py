import pandas as pd
from fastapi import HTTPException

from .entities import HeartDiseaseModel

N_FEATURES = 13
FEATURES = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal"
]


def prepare_and_validate_data(request: HeartDiseaseModel):
    if request.features[:N_FEATURES] != FEATURES:
        raise HTTPException(
            status_code=400,
            detail=f"Expected {N_FEATURES} features in the following order: {FEATURES}"
        )
    data = pd.DataFrame(request.data, columns=request.features)
    if "target" in request.features:
        data.drop(columns=["target"], inplace=True)
    return data

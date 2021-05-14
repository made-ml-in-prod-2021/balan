import pickle
import logging
from typing import Dict, Union, Tuple

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score

from ..params.train_params import TrainingParams


logger = logging.getLogger(__name__)
SklearnClassifier = Union[RandomForestClassifier, LogisticRegression]


def fit_model(
    features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> SklearnClassifier:
    if train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(
            n_estimators=train_params.n_estimators,
            random_state=train_params.random_state,
        )
    elif train_params.model_type == "LogisticRegression":
        model = LogisticRegression()
    else:
        raise NotImplementedError()
    model.fit(features, target)
    logger.info(f"Fitted model of type {train_params.model_type}")
    return model


def predict_model(
    model: SklearnClassifier,
    features: pd.DataFrame
) -> Tuple[np.ndarray, np.ndarray]:
    predicted = model.predict(features)
    predicted_proba = model.predict_proba(features)[:, 1]
    logger.info(f"Made prediction")
    return predicted, predicted_proba


def evaluate_model(
    predicted: np.ndarray,
    predicted_proba: np.ndarray,
    target: pd.Series
) -> Dict[str, float]:
    return {
        "accuracy_score": accuracy_score(target, predicted),
        "roc_auc_score": roc_auc_score(target, predicted_proba),
        "f1_score": f1_score(target, predicted)
    }


def serialize_model(model: SklearnClassifier, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    logger.info(f"Model is saved by path {output}")
    return output

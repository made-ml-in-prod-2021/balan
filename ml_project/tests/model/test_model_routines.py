import os
import pickle
from typing import Tuple
import pytest

import pandas as pd
from sklearn.linear_model import LogisticRegression

from src.params import TransformerParams, TrainingParams
from src.features import split_features_target, DataTransformer
from src.model import fit_model, predict_model, serialize_model


@pytest.fixture
def features_and_target(
    synth_dataset: pd.DataFrame, transformer_params: TransformerParams, target_name: str
) -> Tuple[pd.DataFrame, pd.Series]:
    features, target = split_features_target(synth_dataset, target_name)
    transformer = DataTransformer(transformer_params).fit(features, target)
    features, target = transformer.transform(features, target)
    return features, target


def test_fit_predict_model(features_and_target: Tuple[pd.DataFrame, pd.Series]):
    features, target = features_and_target
    model = fit_model(features, target, train_params=TrainingParams())
    predicted, predicted_proba = predict_model(model, features)
    assert isinstance(model, LogisticRegression)
    assert predicted.shape == target.shape
    assert predicted_proba.shape == target.shape


def test_serialize_model(tmpdir):
    expected_output = tmpdir.join("model.pkl")
    model = LogisticRegression()
    real_output = serialize_model(model, expected_output)
    assert real_output == expected_output
    assert os.path.exists(real_output)
    with open(real_output, "rb") as f:
        model = pickle.load(f)
    assert isinstance(model, LogisticRegression)

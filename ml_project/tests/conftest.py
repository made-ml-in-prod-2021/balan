import os
import pytest
import pandas as pd
from src.params import TransformerParams
from tests.utils import make_synthetic_data


@pytest.fixture()
def dataset_path():
    tests_dir = os.path.dirname(__file__)
    return os.path.join(tests_dir, "small_heart.csv")


@pytest.fixture()
def target_name():
    return "target"


@pytest.fixture()
def synth_dataset() -> pd.DataFrame:
    synth_data = make_synthetic_data()
    return synth_data


@pytest.fixture()
def transformer_params() -> TransformerParams:
    return TransformerParams(use_scaler=True)

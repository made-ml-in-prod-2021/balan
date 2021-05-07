import pandas as pd
from src.features.make_features import split_features_target


def test_split_features_target(synth_dataset: pd.DataFrame, target_name: str):
    data, target = split_features_target(synth_dataset, target_name)
    assert len(data) == len(target) == len(synth_dataset)
    assert isinstance(target, pd.Series)
    assert data.shape[1] == synth_dataset.shape[1] - 1

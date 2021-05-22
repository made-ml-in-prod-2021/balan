import pandas as pd

from src.features import DataTransformer, split_features_target
from src.params import TransformerParams


def test_data_transformer(
    synth_dataset: pd.DataFrame,
    transformer_params: TransformerParams,
    target_name: str,
):
    features, target = split_features_target(synth_dataset, target_name)
    transformer = DataTransformer(transformer_params).fit(features, target)
    transformed_features, transformed_target = transformer.transform(features, target)
    assert transformed_features.shape == features.shape
    assert len(transformed_target) == len(target)

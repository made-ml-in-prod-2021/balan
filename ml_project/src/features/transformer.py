import pickle
import logging
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
from src.params import TransformerParams


logger = logging.getLogger(__name__)


class DataTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, params: TransformerParams):
        self.params = params
        self.scaler = StandardScaler()

    def fit(self, features: pd.DataFrame, target: pd.Series = None):
        if self.params.use_scaler:
            self.scaler.fit(features)
        return self

    def transform(self, features: pd.DataFrame, target: pd.Series = None):
        if self.params.use_scaler:
            transformed_features = self.scaler.transform(features)
        else:
            transformed_features = features.to_numpy()
        return transformed_features, target

    def save(self, output: str) -> str:
        with open(output, "wb") as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
        logger.info(f"Transformer is saved by path {output}")
        return output

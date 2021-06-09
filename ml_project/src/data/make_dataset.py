import logging
from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split

from ..params import SplittingParams


logger = logging.getLogger(__name__)


def load_data(path: str) -> pd.DataFrame:
    logger.info(f"Started loading data from {path}")
    data = pd.read_csv(path)
    logger.info("Finished loading data")
    return data


def split_train_val_data(
    data: pd.DataFrame, splitting_params: SplittingParams,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    logger.info("Started splitting data...")
    train_data, val_data = train_test_split(
        data,
        test_size=splitting_params.test_size,
        random_state=splitting_params.random_state,
    )
    logger.info("Finished splitting data")
    return train_data, val_data

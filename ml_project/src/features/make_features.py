import logging
from typing import Tuple

import pandas as pd


logger = logging.getLogger(__name__)


def split_features_target(
    data: pd.DataFrame, target_name: str
) -> Tuple[pd.DataFrame, pd.Series]:
    logger.info("Started feature-target splitting...")
    features = data.drop(columns=[target_name])
    target = data[target_name]
    logger.info("Finished feature-target splitting")
    return features, target

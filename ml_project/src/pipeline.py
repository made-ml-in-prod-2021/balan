import sys
import json
import logging

import click

from .data import load_data, split_train_val_data
from .params.pipeline_params import PipelineParams, read_training_pipeline_params
from .features import split_features_target, DataTransformer
from .model import (
    fit_model,
    predict_model,
    evaluate_model,
    serialize_model,
)

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def train_pipeline(params: PipelineParams):
    logger.info(f"Started training pipeline with params {params}")
    data = load_data(params.input_data_path)
    logger.info(f"data.shape is {data.shape}")
    train_df, val_df = split_train_val_data(
        data, params.splitting_params
    )
    logger.info(f"train_df.shape is {train_df.shape}")
    logger.info(f"val_df.shape is {val_df.shape}")

    train_features, train_target = split_features_target(train_df, params.target_name)
    transformer = DataTransformer(params.transformer_params).fit(
        train_features,
        train_target,
    )
    transformer.save(params.transformer_path)

    train_features, train_target = transformer.transform(train_features, train_target)
    logger.info(f"train_features.shape is {train_features.shape}")

    model = fit_model(
        train_features, train_target, params.train_params
    )
    val_features, val_target = split_features_target(val_df, params.target_name)
    val_features, val_target = transformer.transform(val_features, val_target)
    logger.info(f"val_features.shape is {val_features.shape}")

    predicted, predicted_proba = predict_model(model, val_features)
    metrics = evaluate_model(
        predicted=predicted,
        predicted_proba=predicted_proba,
        target=val_target,
    )

    with open(params.metric_path, "w") as metric_file:
        json.dump(metrics, metric_file)
    logger.info(f"Validation metrics: {metrics}")
    path_to_model = serialize_model(model, params.output_model_path)

    return path_to_model, metrics


@click.command(name="pipeline")
@click.argument("config_path")
def main(config_path: str):
    params = read_training_pipeline_params(config_path)
    train_pipeline(params)


if __name__ == "__main__":
    main()

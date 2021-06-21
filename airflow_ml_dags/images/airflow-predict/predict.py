import os
import pickle
import logging

import click
import pandas as pd


logger = logging.getLogger("predict")


@click.command("predict")
@click.option("--input-dir", required=True)
@click.option("--output-dir", required=True)
@click.option("--model-path", required=True)
def predict(input_dir: str, output_dir: str, model_path: str):

    data = pd.read_csv(os.path.join(input_dir, "data.csv"))

    with open(model_path, "rb") as f:
        model = pickle.load(f)

    y_pred = model.predict(data)
    data = pd.DataFrame(y_pred, columns=["target"])
    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, "predictions.csv"), index=False)

    logger.info("Prediction ready")


if __name__ == '__main__':
    predict()

import os
import pickle
import logging
import json

import click
import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score, f1_score


logger = logging.getLogger("validate")


@click.command("download")
@click.option("--input-dir", required=True)
@click.option("--models-dir", required=True)
def validate(input_dir: str, models_dir: str):

    with open(os.path.join(models_dir, "model.pkl"), "rb") as f:
        model = pickle.load(f)

    val_data = pd.read_csv(os.path.join(input_dir, "val.csv"))
    y_val = val_data[['target']].values
    x_val = val_data.drop(columns=['target'])

    y_pred = model.predict(x_val)

    metrics = {
        "accuracy_score": accuracy_score(y_val, y_pred),
        "roc_auc_score": roc_auc_score(y_val, y_pred),
        "f1_score": f1_score(y_val, y_pred),
    }

    with open(os.path.join(models_dir, "metrics.json"), "w") as f:
        json.dump(metrics, f)

    logger.info("Validation completed")


if __name__ == "__main__":
    validate()

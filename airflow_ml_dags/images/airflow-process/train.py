import os
import pickle
import logging

import click
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


logger = logging.getLogger("train")


@click.command("download")
@click.option("--input-dir", required=True)
@click.option("--models-dir", required=True)
def train(input_dir: str, models_dir: str):

    train_data = pd.read_csv(os.path.join(input_dir, "train.csv"))
    y_train = train_data[['target']]
    x_train = train_data.drop(columns=['target'])

    model = RandomForestClassifier(max_depth=10)
    model.fit(x_train, y_train)

    os.makedirs(models_dir, exist_ok=True)
    with open(os.path.join(models_dir, "model.pkl"), "wb") as f:
        pickle.dump(model, f)

    logger.info("Training completed")


if __name__ == '__main__':
    train()

import os
import logging

import click
import pandas as pd
from sklearn.model_selection import train_test_split


logger = logging.getLogger("split")


@click.command()
@click.option("--input-dir")
def split(input_dir: str):

    data = pd.read_csv(os.path.join(input_dir, "train_data.csv"))
    train_data, val_data = train_test_split(data, test_size=0.2)

    train_data.to_csv(os.path.join(input_dir, "train.csv"), index=False)
    val_data.to_csv(os.path.join(input_dir, "val.csv"), index=False)

    logger.info("Train/validation splitting completed")


if __name__ == '__main__':
    split()
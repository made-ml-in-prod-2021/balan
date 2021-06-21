import os
import logging

import click
import numpy as np
import pandas as pd


logger = logging.getLogger("download")


@click.command("download")
@click.option("--output-dir", required=True)
def download(output_dir: str):
    size = np.random.randint(100, 200)
    data = pd.DataFrame()
    data["age"] = np.random.normal(loc=55, scale=10, size=size)
    data["sex"] = np.random.binomial(n=1, p=0.7, size=size)
    data["cp"] = np.random.randint(low=0, high=4, size=size)
    data["trestbps"] = np.random.normal(loc=130, scale=20, size=size)
    data["chol"] = np.random.normal(loc=250, scale=50, size=size)
    data["fbs"] = np.random.binomial(n=1, p=0.2, size=size)
    data["restecg"] = np.random.choice([0, 1, 2], size=size, p=[0.48, 0.48, 0.04])
    data["thalach"] = np.random.normal(loc=150, scale=20, size=size)
    data["exang"] = np.random.binomial(n=1, p=0.33, size=size)
    data["oldpeak"] = np.clip(
        np.random.normal(loc=1, scale=2, size=size), a_min=0, a_max=None
    ).round(1)
    data["slope"] = np.random.choice([0, 1, 2], size=size, p=[0.08, 0.46, 0.46])
    data["ca"] = np.random.poisson(lam=0.5, size=size)
    data["thal"] = np.random.choice([0, 1, 2, 3], size=size, p=[0.01, 0.07, 0.52, 0.4])
    target = pd.Series(np.random.binomial(n=1, p=0.55, size=size))
    data = data.astype(np.int64)

    os.makedirs(output_dir, exist_ok=True)
    data.to_csv(os.path.join(output_dir, "data.csv"), index=False)
    target.to_csv(os.path.join(output_dir, "target.csv"), index=False)

    logger.info("Download step completed")


if __name__ == '__main__':
    download()

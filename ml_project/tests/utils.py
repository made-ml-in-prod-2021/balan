import pandas as pd
import numpy as np


def make_synthetic_data(
        size=30,
        random_seed: int = 13,
        filename_to_save: str = None,
) -> pd.DataFrame:
    np.random.seed(random_seed)
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
    data["slope"] = np.random.choice([0, 1, 2], size=size, p=[0.08, 0.46, 0.46])
    data["ca"] = np.random.poisson(lam=0.5, size=size)
    data["thal"] = np.random.choice([0, 1, 2, 3], size=size, p=[0.01, 0.07, 0.52, 0.4])
    data["target"] = np.random.binomial(n=1, p=0.55, size=size)
    data = data.astype(np.int64)
    data["oldpeak"] = np.clip(
        np.random.normal(loc=1, scale=2, size=size), a_min=0, a_max=None
    ).round(1)
    if filename_to_save is not None:
        import os
        tests_dir = os.path.dirname(__file__)
        data.to_csv(os.path.join(tests_dir, filename_to_save), index=False)
    return data

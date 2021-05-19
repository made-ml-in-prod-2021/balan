import pickle

from sklearn.pipeline import Pipeline


def load_model_from_path(model_path: str) -> Pipeline:
    with open(model_path, "rb") as f:
        return pickle.load(f)

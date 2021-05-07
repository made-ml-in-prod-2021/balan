import click
import pickle
import pandas as pd

from src.data import load_data
from src.features import split_features_target
from src.model import predict_model


def predict_process(model, transformer, data: pd.DataFrame) -> pd.Series:
    features, _ = split_features_target(data, target_name="target")
    features, _ = transformer.transform(features)
    prediction = predict_model(model, features)
    return pd.Series(prediction, name="prediction")


@click.command()
@click.option("-i", "--input_path", default="data/raw/heart.csv")
@click.option("-o", "--output_path", default="data/out/prediction.csv")
@click.option("-m", "--model_path", default="models/model.pkl")
@click.option("-t", "--transformer_path", default="models/transformer.pkl")
def main(input_path, output_path, model_path, transformer_path):
    data = load_data(input_path)
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    with open(transformer_path, "rb") as transformer_file:
        transformer = pickle.load(transformer_file)
    predictions = predict_process(model, transformer, data)
    predictions.to_csv(output_path, index_label="index")


if __name__ == "__main__":
    main()

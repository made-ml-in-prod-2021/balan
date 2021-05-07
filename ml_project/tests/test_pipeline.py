import os

from src import train_pipeline
from src.params import (
    SplittingParams,
    TransformerParams,
    TrainingParams,
    PipelineParams,
)


def test_train_pipeline(
    tmpdir,
    dataset_path: str,
    target_name: str,
):
    expected_output_model_path = tmpdir.join("model.pkl")
    expected_transformer_path = tmpdir.join("transformer.pkl")
    expected_metric_path = tmpdir.join("metrics.json")

    params = PipelineParams(
        input_data_path=dataset_path,
        output_model_path=expected_output_model_path,
        transformer_path=expected_transformer_path,
        target_name=target_name,
        metric_path=expected_metric_path,
        splitting_params=SplittingParams(
            test_size=0.2,
            random_state=13,
        ),
        transformer_params=TransformerParams(
            use_scaler=True,
        ),
        train_params=TrainingParams(
            model_type="LogisticRegression",
        ),
    )
    real_path_to_model, metrics = train_pipeline(params)
    assert metrics["accuracy_score"] > 0.7
    assert metrics["roc_auc_score"] > 0.7
    assert os.path.exists(real_path_to_model)
    assert os.path.exists(params.output_model_path)
    assert os.path.exists(params.transformer_path)
    assert os.path.exists(params.metric_path)

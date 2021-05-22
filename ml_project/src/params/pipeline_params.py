import yaml
from dataclasses import dataclass

from marshmallow_dataclass import class_schema

from .split_params import SplittingParams
from .transformer_params import TransformerParams
from .train_params import TrainingParams


@dataclass
class PipelineParams:
    input_data_path: str
    output_model_path: str
    transformer_path: str
    target_name: str
    metric_path: str
    splitting_params: SplittingParams
    transformer_params: TransformerParams
    train_params: TrainingParams


PipelineParamsSchema = class_schema(PipelineParams)


def read_training_pipeline_params(path: str) -> PipelineParamsSchema:
    with open(path, "r") as input_stream:
        schema = PipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))

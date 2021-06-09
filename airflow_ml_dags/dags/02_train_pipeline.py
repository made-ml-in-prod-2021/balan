import os

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor

from .constants import DEFAULT_ARGS, START_DATE, DATA_VOLUME_DIR, \
    DATA_RAW_DIR, DATA_PROCESSED_DIR, DATA_MODELS_DIR, VAL_SIZE


with DAG(
    "02_train_pipeline",
    default_args=DEFAULT_ARGS,
    start_date=START_DATE,
    default_view="graph",
    schedule_interval="@weekly",
) as dag:

    start_pipeline = DummyOperator(task_id='start-pipeline')

    wait_data = FileSensor(
        task_id="wait-for-data",
        filepath=str(os.path.join(DATA_RAW_DIR, "data.csv")),
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke",
    )

    wait_target = FileSensor(
        task_id="wait-for-target",
        filepath=str(os.path.join(DATA_RAW_DIR, "target.csv")),
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke",
    )

    data_preprocessing = DockerOperator(
        image="airflow-process",
        command=f"--input-dir {DATA_RAW_DIR} --output-dir {DATA_PROCESSED_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        task_id="data-preprocessing",
        volumes=[f"{DATA_VOLUME_DIR}:/data"],
        entrypoint="python preprocess.py"
    )

    data_split = DockerOperator(
        image="airflow-process",
        command=f"--input-dir {DATA_PROCESSED_DIR} --val-size {VAL_SIZE}",
        network_mode="bridge",
        do_xcom_push=False,
        task_id="data-split",
        volumes=[f"{DATA_VOLUME_DIR}:/data"],
        entrypoint="python split.py"
    )

    model_training = DockerOperator(
        image="airflow-process",
        command=f"--input-dir {DATA_PROCESSED_DIR} --models-dir {DATA_MODELS_DIR}}",
        network_mode="bridge",
        do_xcom_push=False,
        task_id="model-training",
        volumes=[f"{DATA_VOLUME_DIR}:/data"],
        entrypoint="python train.py"
    )

    model_validation = DockerOperator(
        image="airflow-process",
        command=f"--input-dir {DATA_PROCESSED_DIR} --models-dir {DATA_MODELS_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        task_id="model-validation",
        volumes=[f"{DATA_VOLUME_DIR}:/data"],
        entrypoint="python validate.py"
    )

    start_pipeline >> [wait_data, wait_target] >> data_preprocessing >> \
        data_split >> model_training >> model_validation

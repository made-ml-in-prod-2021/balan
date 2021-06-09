import os

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.sensors.filesystem import FileSensor

from .constants import DEFAULT_ARGS, START_DATE, DATA_VOLUME_DIR, \
    DATA_RAW_DIR, DATA_PREDICTIONS_DIR, MODEL_PATH


with DAG(
    "03_predict",
    default_args=DEFAULT_ARGS,
    start_date=START_DATE,
    schedule_interval="@daily",
) as dag:

    start_predict = DummyOperator(task_id='start-predict')

    wait_data = FileSensor(
        task_id="wait-for-data",
        filepath=str(os.path.join(DATA_RAW_DIR, "data.csv")),
        timeout=6000,
        poke_interval=10,
        retries=100,
        mode="poke",
    )

    make_prediction = DockerOperator(
        image="airflow-predict",
        command=f"--input-dir {DATA_RAW_DIR} --output-dir {DATA_PREDICTIONS_DIR} --model-path {MODEL_PATH}",
        network_mode="bridge",
        do_xcom_push=False,
        task_id="make-prediction",
        volumes=[f"{DATA_VOLUME_DIR}:/data"]
    )

    start_predict >> wait_data >> make_prediction

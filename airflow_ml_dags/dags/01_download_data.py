from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.providers.docker.operators.docker import DockerOperator

from .constants import DEFAULT_ARGS, START_DATE, DATA_RAW_DIR, DATA_VOLUME_DIR


with DAG(
    "01_download_data",
    default_args=DEFAULT_ARGS,
    start_date=START_DATE,
    schedule_interval="@daily",
) as dag:

    start_download = DummyOperator(task_id="start-download")

    data_download = DockerOperator(
        image="airflow-download",
        command=f"--output-dir {DATA_RAW_DIR}",
        network_mode="bridge",
        do_xcom_push=False,
        task_id="download-data",
        volumes=[f"{DATA_VOLUME_DIR}:/data"],
    )

    start_download >> data_download

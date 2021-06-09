from datetime import timedelta

from airflow.models import Variable
from airflow.utils.dates import days_ago


DEFAULT_ARGS = {
    'owner': 'airflow',
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1),
}

START_DATE = days_ago(7)

DATA_RAW_DIR = "/data/raw/{{ ds }}"
DATA_PROCESSED_DIR = "/data/processed/{{ ds }}"
DATA_MODELS_DIR = "/data/models/{{ ds }}"
DATA_PREDICTIONS_DIR = "/data/predictions/{{ ds }}"

MODEL_PATH = Variable.get("model_path")
# MODEL_PATH = os.environ["MODEL_PATH"]

VAL_SIZE = 0.2
RANDOM_SEED = 13

DATA_VOLUME_DIR = "/Users/Artur/PycharmProjects/ml-in-prod-hw3/data"

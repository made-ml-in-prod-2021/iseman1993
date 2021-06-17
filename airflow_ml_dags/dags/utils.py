from datetime import timedelta

DEFAULT_VOLUME = '/home/nika/PycharmProjects/airflow_ml_dags/data:/data'

default_args = {
    'owner': 'Nika Kishmaria',
    'depends_on_past': False,
    'email': ['ngkishmaria@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

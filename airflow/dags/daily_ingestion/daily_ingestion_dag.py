from airflow import DAG
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {
    'owner': 'Ajay',
    'depends_on_past': False,
    'email': ['junioralexio607@gmail.com.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 5, 24),
    'end_date': datetime(2024, 7, 27),
    'schedule_interval': '@daily'
}

with DAG(
    'daily_ingestion_dag',
    default_args=default_args,
    description='A simple ETL job using Bash commands',
) as dag:

    t1 = BashOperator(
                task_id="t1",
                bash_command="echo 'This is task no1 '",
            )

    t2 = BashOperator(
                task_id="t2",
                bash_command="echo 'This is task no2 '",
            )

t1 >> t2
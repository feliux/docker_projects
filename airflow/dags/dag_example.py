import logging
import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def log_hello_world():
    logging.info("Hello world!")
    

default_args = {
        "owner":"airflow",
        "depends_on_past":"false",
        "start_date":datetime.today()-timedelta(days=1),
}

dag = DAG(
    dag_id="dag_hello_world", 
    default_args=default_args, 
    schedule_interval=timedelta(seconds=30)
)

task = PythonOperator(
    task_id="task_hello_world",
    python_callable=log_hello_world,
    dag=dag,
)

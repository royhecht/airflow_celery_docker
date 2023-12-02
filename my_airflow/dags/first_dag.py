from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from my_airflow.dag_functions import extract_data, transform_and_load

default_args = {
    'owner': 'my_airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
        'example_dag',
        default_args=default_args,
        description='A simple example DAG') as dag:

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract_data,
        provide_context=True,
    )

    transform_load_task = PythonOperator(
        task_id='transform_load_task',
        python_callable=transform_and_load,
        provide_context=True,
    )


    ### send to database/other processing repo - function

    extract_task >> transform_load_task

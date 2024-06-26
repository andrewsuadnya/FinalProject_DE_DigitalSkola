from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import finnhub_mongodb_loader
import sentiment_analysis_loader



default_args = {
    'owner': 'de-team',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 21),
    'wait_for_downstream': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'sla': timedelta(days=1),
}

schedule_interval = '0 0 * * *'

with DAG(
    'dag_sentiment_analysis',
    default_args=default_args,
    schedule_interval=schedule_interval,
    catchup=False,
    tags=['machine-learning']
) as dag:
    extract_load = PythonOperator(
        task_id=f'extract_load',
        python_callable=finnhub_mongodb_loader.extract_load
    )

    sa_load = PythonOperator(
        task_id=f'sa_load',
        python_callable=sentiment_analysis_loader.run
    )

    extract_load >> sa_load

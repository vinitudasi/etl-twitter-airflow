import os
from dotenv import load_dotenv

from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from twitter_etl import run_twitter_etl

# Load environment variables from .env file
load_dotenv()
EMAIL = os.getenv("EMAIL")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020,11,8),
    'email': [EMAIL],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Define the DAG
twitter_dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Twitter Data ETL'
)

# Define the PythonOperator to run the ETL function
run_etl = PythonOperator(
    task_id='run_twitter_etl',
    python_callable=run_twitter_etl,
    dag=twitter_dag
)

# Set task in the DAG
run_etl

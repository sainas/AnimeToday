import boto3
import io


# airflow related
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

# other packages
from datetime import datetime
from datetime import timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 2, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}


dag = DAG(
  dag_id='animetodaycrawling',
  description='Simple tutorial DAG',
  schedule_interval = '00 09 * * *',
  default_args=default_args)
crawling = BashOperator(
  task_id='crawling',
  bash_command='python /home/ubuntu/Insight/AnimeToday/Repo/newrepo/Crawling.py',
  dag = dag)


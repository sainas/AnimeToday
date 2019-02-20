# import pandas as pd
# import boto3
# import io


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
    'start_date': datetime(2019, 9, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'schedule_interval': '@daily',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}


def read_s3():
    file2 = open('~/Insight/output/testfile.txt','w') 
    file2.write('Hello World') 
    file2.write('This is our new text file') 
    file2.write('and this is another line.') 
    file2.write('Why? Because we can.') 
    file.close() 


def read_s3true():
    s3 = boto3.resource('s3')
    obj = s3.Object('sainabuckettest', 'h1b_input.csv')
    obj.get()['Body'].read().decode('utf-8') 
    file = open('~/Insight/output/s33.txt','w') 
    file.write('readfile') 
    file.close()

dag = DAG(
  dag_id='AnimeToday',
  description='Simple tutorial DAG',
  default_args=default_args)

task1 = BashOperator(
  task_id='pool_data',
  bash_command='',
  dag = dag)

task21 = BashOperator(
  task_id='update_anime',
  bash_command='',
  dag = dag)

task22 = BashOperator(
  task_id='update_episode',
  bash_command='',
  dag = dag)

task3 = BashOperator(
  task_id='notify_by_email_and_sms',
  bash_command='',
  dag = dag)



# setting dependencies
task1 >> task21
task1 >> task22
task21 >>task3
task22 >> task3

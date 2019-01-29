import pandas as pd
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
    'start_date': datetime(2018, 9, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'schedule_interval': '@daily',
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}


def read_s3():
    file2 = open(“~/Insight/output/testfile.txt”,”w”) 
    file2.write('Hello World) 
    file2.write('This is our new text file) 
    file2.write('and this is another line.) 
    file2.write('Why? Because we can.') 
    file.close() 


def read_s3true():
    s3 = boto3.resource('s3')
    obj = s3.Object('sainabuckettest', 'h1b_input.csv')
    obj.get()['Body'].read().decode('utf-8') 
    file = open(“~/Insight/output/s33.txt”,”w”) 
    file.write('readfile') 
    file.close()

dag = DAG(
  dag_id='my_dag', 
  description='Simple tutorial DAG',
  default_args=default_args)

createfolder00 = BashOperator(
  task_id='createfolder00',
  bash_command='/home/sainas/Documents/Insight/',
  dag = dag)

createfolder0 = BashOperator(
  task_id='createfolder0',
  bash_command='mkdir ~/Insight',
  dag = dag)

createfolder11 = BashOperator(
  task_id='createfolder11',
  bash_command='mkdir ~/Insight/src',
  dag = dag)

createfolder12 = BashOperator(
  task_id='createfolder12',
  bash_command='mkdir ~/Insight/input',
  dag = dag)

createfolder13 = BashOperator(
  task_id='createfolder13',
  bash_command='mkdir ~/Insight/output',
  dag = dag)

loadfile = PythonOperator(
  task_id='loadfile',
  python_callable=read_s3,
  dag = dag)

loadfiletrue = PythonOperator(
  task_id='loadfiletrue',
  python_callable=read_s3true,
  dag = dag)

# setting dependencies
createfolder00 >> createfolder0
createfolder0 >> createfolder11
createfolder0 >> createfolder12
createfolder0 >> createfolder13
createfolder11 >> loadfile
createfolder12 >> loadfile
createfolder13 >> loadfile
loadfile>>loadfiletrue
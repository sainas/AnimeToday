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
    'start_date': datetime(2019, 2, 24),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(seconds=5),
}


dag = DAG(
  dag_id='animetoday_without_crawling',
  description='animetoday_without_crawling',
  schedule_interval = '00 08 * * *',
  default_args=default_args)


updating1 = BashOperator(
  task_id='update_anime',
  bash_command='python3 /home/ubuntu/AnimeToday/src/update_anime.py',
  dag = dag)
  
updating2 = BashOperator(
  task_id='update_episode',
  bash_command='python3 /home/ubuntu/AnimeToday/src/update_episode.py',
  dag = dag)
  
updating3 = BashOperator(
  task_id='update_pic_url',
  bash_command='python3 /home/ubuntu/AnimeToday/src/update_pic_url.py',
  dag = dag)
  
notifying = BashOperator(
  task_id='notify_by_email_and_sms',
  bash_command='python3 /home/ubuntu/AnimeToday/src/notify_by_email_and_sms.py',
  dag = dag)
  

updating1 >> updating2
updating1 >> updating3
updating2 >> notifying
updating3 >> notifying
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

seven_days_ago = datetime.combine(datetime.today() - timedelta(7),
                                                                  datetime.min.time())

default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2024,2,1),
        'email': ['jfibanezquiroz@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
  }

dag = DAG(dag_id='prueba_jose', default_args=default_args, schedule_interval='2 * * * *')
t1 = BashOperator(
    task_id='Extract',
    bash_command='python /opt/airflow/codigo/Extract.py',
    dag=dag)
t2 = BashOperator(
    task_id='Transform',
    bash_command='python /opt/airflow/codigo/Transform.py',
    dag=dag)

t3 = BashOperator(
    task_id='Verify',
    bash_command='python /opt/airflow/codigo/verify.py',
    dag=dag)

t4 = BashOperator(
    task_id='Load',
    bash_command='python /opt/airflow/codigo/Load.py',
    dag=dag)



t1 >> t2
# t1>>t2>>t3>>t4
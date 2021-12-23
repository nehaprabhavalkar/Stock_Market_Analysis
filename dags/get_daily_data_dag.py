from airflow.models.dag import dag
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from datetime import datetime, time, timedelta
from airflow.utils.trigger_rule import TriggerRule
from airflow import DAG, AirflowException
import subprocess
import json

START_DATE = datetime.now() - timedelta(minutes=1470)

with open('config.json') as file:
  config_data = json.load(file)

holiday_script_path = config_data['holiday_script_path']

execute_script_cmd = f"python {holiday_script_path}"

def validate_day():
    # code for holiday check
    pass

default_args = {

    'owner': "Neha",
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': START_DATE,
    'end_date': datetime(2099,12,31),
    'retry_delay': timedelta(minutes=1),
    'retries': 0,
    'concurrency': 1

}

dag_obj = DAG('get_daily_data_dag', max_active_runs=1, schedule_interval=None, catchup=False, default_args=default_args)

start_task = DummyOperator(task_id="start", dag=dag_obj)

validate_day_task = BranchPythonOperator(task_id="validate_day", python_callable=validate_day, dag=dag_obj)

run_script = BashOperator(task_id="run_script", bash_command=execute_script_cmd, dag=dag_obj)

invalid_day = DummyOperator(task_id="invalid_day", dag=dag_obj)

end_task = DummyOperator(task_id="end", dag=dag_obj, trigger_rule=TriggerRule.ONE_SUCCESS)

start_task >> validate_day_task >> run_script >> end_task
validate_day_task >> invalid_day >> end_task
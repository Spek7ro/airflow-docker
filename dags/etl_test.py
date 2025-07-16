from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="test_dag_bash",
    start_date=datetime(2025, 7, 1),
    schedule="@daily",
    catchup=False,
    tags=["test"]
) as dag:

    tarea = BashOperator(
        task_id="imprimir_fecha",
        bash_command="date"
    )

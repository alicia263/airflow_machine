
FROM apache/airflow:2.7.3

USER root
RUN apt-get update && apt-get install -y gcc g++ make
RUN apt-get install -y gosu


USER airflow





RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" apache-airflow-providers-mongo pandas

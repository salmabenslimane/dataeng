#!/bin/bash
# wait-for-db.sh
: "${AIRFLOW_DB_HOST:=postgres}"
: "${AIRFLOW_DB_PORT:=5432}"

echo "Waiting for Postgres at $AIRFLOW_DB_HOST:$AIRFLOW_DB_PORT..."

# Wait until Airflow can reach the database
until airflow db check; do
  echo "Database not ready, sleeping 2s..."
  sleep 2
done

echo "Database ready, starting Airflow..."
exec "$@"

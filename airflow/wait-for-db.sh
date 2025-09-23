#!/bin/bash
# wait-for-db.sh

# Default values
: "${AIRFLOW_DB_HOST:=postgres}"
: "${AIRFLOW_DB_PORT:=5432}"

echo "Waiting for Postgres at $AIRFLOW_DB_HOST:$AIRFLOW_DB_PORT..."

# Loop until Postgres responds
until pg_isready -h "$AIRFLOW_DB_HOST" -p "$AIRFLOW_DB_PORT" -U "airflow"; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Postgres is up - starting Airflow"

# Run the command passed to the container
exec "$@"

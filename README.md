📂 Overview 

Programming Language: Python
Data Sources: Mock API (Mockaroo)
Storage: DuckDB
Orchestration: Airflow (Airflow DAG runs your CLI tools (init-db.py, fetch-data.py) on a schedule → updates DuckDB)


📂 DB Folder Structure 

init\db/
├── raw_data.duckdb         ← The actual DuckDB database file
├── init_schema.py          ← Script to define your schema (raw.orders, raw.users, etc.)
├── fetch_and_insert.py     ← Script to fetch from API and insert into DuckDB
└── config.json             ← Store API URLs, keys, etc.


📂 Iterations: 

Iteration 1: Create all the functional code 
Iteration 2: Turn following files into CLI tools (init-db.py)

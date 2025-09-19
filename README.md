 📂 Overview 

| Mini-project (Mockaroo)            | Air France real use case                              |
| ---------------------------------- | ----------------------------------------------------- |

| Random new data every API call     | New flight bookings, cancellations, check-ins         |

| You fetch periodically via Airflow | Automated ETL pipeline fetching new events            |

| Insert into DuckDB                 | Insert into production warehouse (BigQuery/Snowflake) |

| Raw schema stays the same          | Raw tables always have same structure                 |

----------------------------------------------------------------------------------------------

* Programming Language: Python
* Data Sources: Mock API (Mockaroo)
* Storage: DuckDB
* Orchestration: Airflow (Airflow DAG runs your CLI tools (init-db.py, fetch-data.py) on a schedule → updates DuckDB)
* Stream : API → DuckDB → Airflow → Streamlit

📂 Iterations: 

Iteration 1: Create all the functional code 
Iteration 2: Turn following files into CLI tools (init-db.py and fetch-data.py)


📂 DB Folder Structure 

mini_data_pipeline/
├── db/
│   ├── raw_data.duckdb           # Your DuckDB database file
│   ├── init_schema.py            # Create schemas & tables
│   ├── fetch_and_insert.py       # Fetch data from API & insert
│   └── db_connection.py          # Helper to connect to DuckDB
│
├── dags/
│   └── etl_pipeline.py           # Airflow DAG orchestrating ETL
│
├── config/
│   └── config.json               # API URLs, keys, etc.
│
├── cli_tools/
│   ├── init-db.py                # CLI wrapper for init_schema.py
│   └── fetch-data.py             # CLI wrapper for fetch_and_insert.py
│
├── dashboard/
│   └── app.py                    # Streamlit dashboard
│
├── requirements.txt              # All Python dependencies
└── README.md                     # Project description & instructions

📂 Features of API data: 

Booking_ID	
Booking_Date
Flight_ID	
Flight_Date
Passenger_ID	
Passenger_Name	
Email	
Gender  
Country_Code	
Ticket_Class	
Quantity	
Unit_Price	
Payment_Method	
Booking_Status	
Revenue


📂 Overview 
API → DuckDB → Airflow → Streamlit

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
Iteration 2: Turn following files into CLI tools (init-db.py and fetch-data.py)



| Mini-project (Mockaroo)            | Air France real use case                              |
| ---------------------------------- | ----------------------------------------------------- |

| Random new data every API call     | New flight bookings, cancellations, check-ins         |

| You fetch periodically via Airflow | Automated ETL pipeline fetching new events            |

| Insert into DuckDB                 | Insert into production warehouse (BigQuery/Snowflake) |

| Raw schema stays the same          | Raw tables always have same structure                 |



🔹 Example row
Booking_ID	Booking_Date	Flight_ID	Flight_Date	Passenger_ID	Passenger_Name	Email	Gender  Country_Code	Ticket_Class	Quantity	Unit_Price	Payment_Method	Booking_Status	Revenue

BKG001	2025-09-18 14:23	AF123	2025-09-25 08:45	PAX001	Alice Dupont	alice.dupont@example.com    Female	FR	Economy	1	120	Credit Card	Confirmed	120
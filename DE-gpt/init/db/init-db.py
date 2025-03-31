import duckdb
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', 
                    handlers=[logging.FileHandler('db_creation.log'), logging.StreamHandler()])

# Function to create the 'raw' schema
def create_raw_schema():
    try:

        # Establish a DuckDB connection (in-memory for this example, you can specify a file for persistence)
        conn = duckdb.connect(database='ecommerce_data.db')
        logging.info("Connected to DuckDB database.")

        # Create the raw schema
        conn.execute("CREATE SCHEMA IF NOT EXISTS raw")
        logging.info("Raw schema created successfully.")

        conn.excecute("""
            CREATE TABLE IF NOT EXISTS raw.orders (
             
                      'schema'
        """)

# Run the function to create the 'raw' schema
create_raw_schema()

# Close the connection
conn.close()

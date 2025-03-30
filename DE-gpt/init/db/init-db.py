import duckdb
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Establish a DuckDB connection (in-memory for this example, you can specify a file for persistence)
conn = duckdb.connect(database=':memory:')

# Function to create the 'raw' schema
def create_raw_schema():
    try:
        # Create the raw schema
        conn.execute("CREATE SCHEMA IF NOT EXISTS raw")
        logger.info("Raw schema created successfully.")
    except Exception as e:
        logger.error(f"Error creating raw schema: {e}")

# Run the function to create the 'raw' schema
create_raw_schema()

# Close the connection
conn.close()

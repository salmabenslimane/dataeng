import duckdb
import requests
import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# API endpoint and key
url = "https://my.api.mockaroo.com/sales"
headers = {"X-API-Key": "e5432ea0"}

# Fetch data from API
try:
    logging.info("📡 Fetching data from API...")
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    logging.info("✅ API data fetched successfully.")
except Exception as e:
    logging.error(f"❌ Error fetching API data: {e}")
    data = []

# Load data into DuckDB
if data:
    df = pd.DataFrame(data)
    logging.info(f"📊 Loaded {len(df)} rows into DataFrame.")

    try:
        conn = duckdb.connect('ecommerce_data.db')
        logging.info("🦆 Connected to DuckDB.")

        # Insert into raw.orders
        conn.execute("CREATE SCHEMA IF NOT EXISTS raw;")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS raw.orders AS 
            SELECT * FROM df
        """)
        logging.info("✅ Table 'raw.orders' created with API data.")
        
        # If you want to *append* instead of overwrite:
        # conn.register("df", df)
        # conn.execute("INSERT INTO raw.orders SELECT * FROM df")

    except Exception as e:
        logging.error(f"❌ Error writing to DuckDB: {e}")
    finally:
        conn.close()
        logging.info("🔒 Connection to DuckDB closed.")
else:
    logging.warning("⚠️ No data fetched from API, skipping DuckDB insert.")

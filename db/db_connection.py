import duckdb
import os

DB_FILE = os.path.join(os.path.dirname(__file__), "raw_data.duckdb")

def get_connection():
    """Return a DuckDB connection."""
    conn = duckdb.connect(DB_FILE)
    return conn   
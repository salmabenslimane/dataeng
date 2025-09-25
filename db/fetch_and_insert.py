import pandas as pd
import requests
from db_connection import get_connection

API_URL = "https://my.api.mockaroo.com/flight_sales.json?key=e5432ea0" # Replace with your Mockaroo API key

def fetch_data():
    """Fetch flight sales data from API and return as DataFrame"""
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data)
    return df

def insert_data(df):
    """Insert DataFrame into DuckDB"""
    con = get_connection()
    con.execute("INSERT INTO raw.flight_sales SELECT * FROM df")
    print(f"{len(df)} rows inserted into DuckDB!")
    con.close()

if __name__ == "__main__":
    df = fetch_data()
    insert_data(df)

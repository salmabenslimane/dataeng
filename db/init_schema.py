from db_connection import get_connection

def init_schema():
    con = get_connection()
    
    # Create schema if it doesn't exist
    con.execute("CREATE SCHEMA IF NOT EXISTS raw;")
    
    # Create table for flight sales
    con.execute("""
        CREATE TABLE IF NOT EXISTS raw.flight_sales (
            booking_id VARCHAR,
            booking_date DATE,
            flight_date DATE,
            passenger_id VARCHAR,
            passenger_name VARCHAR,
            email VARCHAR,
            gender VARCHAR,
            country_code VARCHAR,
            ticket_class VARCHAR,
            quantity INTEGER,
            unit_price DOUBLE,
            revenue DOUBLE
        );
    """)
    print("Schema and table created successfully!")
    con.close()

if __name__ == "__main__":
    init_schema()

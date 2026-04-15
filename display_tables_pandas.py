import sqlite3
import pandas as pd
from tabulate import tabulate

def display_tables():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Query to fetch all table names in the database
    # Filtering out system tables and Django internal tables just to focus on our models
    query = """
    SELECT name FROM sqlite_master 
    WHERE type='table' 
      AND name NOT LIKE 'sqlite_%' 
      AND name NOT LIKE 'django_%' 
      AND name NOT LIKE 'auth_%'
    """
    cursor.execute(query)
    tables = cursor.fetchall()

    print("=========================================================")
    print("                 DATABASE TABLES REPORT                  ")
    print("=========================================================\n")

    for table in tables:
        raw_table_name = table[0]
        # Format table name to look beautiful (e.g., 'startpage_hostel' -> 'Hostel')
        display_name = raw_table_name.replace('startpage_', '').replace('_', ' ').title()
        print(f"--- Table: {display_name} ---")
        try:
            # Read the entire table using pandas
            df = pd.read_sql_query(f"SELECT * FROM {raw_table_name}", conn)
            if df.empty:
                print("No data in this table.\n")
            else:
                # Use tabulate with 'psql' format to render classic SQL-like beautiful tables
                print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
            print("\n" + "="*50 + "\n")
        except Exception as e:
            print(f"Error reading table {display_name}: {e}\n")

    conn.close()

if __name__ == '__main__':
    display_tables()

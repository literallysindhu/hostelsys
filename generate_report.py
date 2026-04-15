import sqlite3
import pandas as pd

def generate_markdown_report():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    query = """
    SELECT name FROM sqlite_master 
    WHERE type='table' 
      AND name NOT LIKE 'sqlite_%' 
      AND name NOT LIKE 'django_%' 
      AND name NOT LIKE 'auth_%'
    """
    cursor.execute(query)
    tables = cursor.fetchall()

    with open('db_report.md', 'w', encoding='utf-8') as f:
        f.write("# Database Tables Report\n\n")
        f.write("Below is the output of all the application specific tables stored in sqlite3.\n\n")

        for table in tables:
            table_name = table[0]
            f.write(f"## Table: {table_name}\n\n")
            try:
                df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
                if df.empty:
                    f.write("*No data in this table.*\n\n")
                else:
                    f.write(df.to_markdown(index=False))
                    f.write("\n\n")
            except Exception as e:
                f.write(f"*Error reading table {table_name}: {e}*\n\n")

    conn.close()

if __name__ == '__main__':
    generate_markdown_report()

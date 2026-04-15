import sqlite3
import pandas as pd
import os

def export_to_excel():
    db_path = 'db.sqlite3'
    excel_path = 'hostel_database_export.xlsx'
    
    conn = sqlite3.connect(db_path)
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
    
    print(f"Exporting data to {excel_path}...")

    # Using ExcelWriter to write multiple sheets into one file
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        for table in tables:
            raw_table_name = table[0]
            # Clean up tab name (Excel allows max 31 characters per sheet name)
            sheet_name = raw_table_name.replace('startpage_', '').title()[:31]
            
            try:
                df = pd.read_sql_query(f"SELECT * FROM {raw_table_name}", conn)
                # Write to the Excel file
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                print(f" -> Exported '{sheet_name}' ({len(df)} rows)")
            except Exception as e:
                print(f" -> Error exporting {raw_table_name}: {e}")

    conn.close()
    print(f"\nSuccess! All tables have been saved to '{os.path.abspath(excel_path)}'.")

if __name__ == '__main__':
    export_to_excel()

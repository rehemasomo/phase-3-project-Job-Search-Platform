import sqlite3

def print_table_contents(cursor, table_name):
    print(f"Contents of {table_name}:")
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(dict(row))
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")

def main():
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # List of tables to check
    tables = ['users', 'job_listings', 'applications', 'saved_searches']

    # Print contents of each table
    for table in tables:
        print_table_contents(cursor, table)

    # Close cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
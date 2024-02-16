import sqlite3

def convert_csv_to_db(csv_file, db_file, table_name):
    # Create a connection to the database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create the table in the database
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (column1 TEXT, column2 TEXT, column3 TEXT)")

    # Read the CSV file and insert the data into the database
    with open(csv_file, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the header row
            row = line.strip().split(',')
            cursor.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", row)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
# Si ma table n'existe pas, je la crée à partir de mon fichier CSV (./defaut/db_base.csv)




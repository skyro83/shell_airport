import sqlite3
import os

def convert_csv(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]

    return header, data

def create_table(header, table_name):
    header = [f'{col} TEXT' for col in header]
    header = ', '.join(header)
    query = f'CREATE TABLE {table_name} ({header})'
    return query
    
def insert_data(data, table_name):
    query = f'INSERT INTO {table_name} VALUES ({", ".join(["?" for _ in range(len(data[0]))])})'
    return query, data

db_file = 'pokemon.db'

if not os.path.exists(db_file):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS pokemon(title, year, score)")  # Modify the table name and columns accordingly
    header, data = convert_csv('pokemon.csv')  # Modify the CSV file path accordingly
    cur.execute(create_table(header, 'pokemon'))  # Modify the table name accordingly
    cur.execute(insert_data(data, 'pokemon'))  # Modify the table name accordingly
    con.commit()
    con.close()

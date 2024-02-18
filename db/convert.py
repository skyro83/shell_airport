import sqlite3
import os

def convert_csv(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        header = lines[0].strip().split(',')
        data = [line.strip().split(',') for line in lines[1:]]
    return header, data

def create_table(header, table_name):
    header = ', '.join([f'"{h}" TEXT' for h in header])
    query = f'CREATE TABLE IF NOT EXISTS {table_name} ({header})'
    return query

def insert_data(data, table_name):
    placeholders = ', '.join('?' * len(data[0]))
    query = f'INSERT INTO {table_name} VALUES ({placeholders})'
    return query, data

db_file = './db/pokemon.db'
csv_file = './db/pokemon.csv'

if not os.path.exists(db_file):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    header, data = convert_csv(csv_file)
    cur.execute(create_table(header, 'pokemon'))
    cur.executemany(*insert_data(data, 'pokemon'))
    con.commit()
    con.close()
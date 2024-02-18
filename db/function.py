import sqlite3

def get_tables(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return tables

def get_table_data(database_path, table_name):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    conn.close()
    return data

def recherche(database_path, table_name, column_name, value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name} = '{value}'")
    data = cursor.fetchall()
    conn.close()
    return data

def add_row(database_path, table_name, values):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} VALUES {values}")
    conn.commit()
    conn.close()
    
def delete_row(database_path, table_name, column_name, value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name} WHERE {column_name} = '{value}'")
    conn.commit()
    conn.close()
    
def update_row(database_path, table_name, column_name, value, new_value):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table_name} SET {column_name} = '{new_value}' WHERE {column_name} = '{value}'")
    conn.commit()
    conn.close()
    
def create_table(database_path, table_name, columns):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
    conn.commit()
    conn.close()
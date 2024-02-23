import sqlite3
database_path = "pokemon.db"
def recherche() :#database_path, table_name, column_name, value):
    conn = sqlite3.connect("pokemon.db")
    cursor = conn.cursor()
    #cursor.execute(f"SELECT * FROM {table_name} WHERE {column_name} = '{value}'")
    cursor.execute("SELECT * FROM pokemon;")
    data = cursor.fetchall()
    conn.close()
    return data

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

db_file = 'pokemon.db'
csv_file = 'pokemon.csv'

if not os.path.exists(db_file):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    header, data = convert_csv(csv_file)
    cur.execute(create_table(header, 'pokemon'))
    cur.executemany(*insert_data(data, 'pokemon'))
    con.commit()
    con.close()


'''
def add_row(database_path, table_name, values):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO {table_name} VALUES ({','.join(values)})")
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
'''    
def display_all():
    conn = sqlite3.connect(database_path)
    print("conn : ", conn)
    cursor = conn.cursor()
    print("cursor : ", cursor)
    cursor.execute("SELECT * FROM pokemon")
    data = cursor.fetchall()
    conn.close()
    return data

print(display_all())
'''
def search_item(database_path):
    table_name = input("Entrez le nom de la table: ")
    column_name = input("Entrez le nom de la colonne: ")
    value = input("Entrez la valeur: ")
    results = recherche(database_path, table_name, column_name, value)
    for result in results:
        print(result)

def modify_item(database_path):
    table_name = input("Entrez le nom de la table: ")
    column_name = input("Entrez le nom de la colonne: ")
    value = input("Entrez la valeur: ")
    new_value = input("Entrez la nouvelle valeur: ")
    update_row(database_path, table_name, column_name, value, new_value)
    print("Modification effectuée avec succès.")

def add_item(database_path):
    table_name = input("Entrez le nom de la table: ")
    values = input("Entrez les valeurs: ")
    add_row(database_path, table_name, values)
    print("Ajout effectué avec succès.")

def delete_item(database_path):
    table_name = input("Entrez le nom de la table: ")
    column_name = input("Entrez le nom de la colonne: ")
    value = input("Entrez la valeur: ")
    delete_row(database_path, table_name, column_name, value)
    print("Suppression effectuée avec succès.")

def create_new_table(database_path):
    table_name = input("Entrez le nom de la table: ")
    columns = input("Entrez les colonnes: ")
    create_table(database_path, table_name, columns)
    print("Table créée avec succès.")

def main():
    while True:
        print("1. Tout afficher")
        print("2. Rechercher")
        print("3. Modifier")
        print("4. Ajouter")
        print("5. Supprimer")
        print("6. Créer une nouvelle table")
        print("7. Retour")
        option = input("Choisissez une option: ")
        if option == "1":
            print(display_all())
        elif option == "2":
            search_item(database_path)
        elif option == "3":
            modify_item(database_path)
        elif option == "4":
            add_item(database_path)
        elif option == "5":
            delete_item(database_path)
        elif option == "6":
            create_new_table(database_path)
        elif option == "7":
            break
        else:
            print("Option non valide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
'''

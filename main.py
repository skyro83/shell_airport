from db.function import get_tables, recherche, update_row, add_row, delete_row, create_table
import sqlite3
from db.function import update_row
database_path = "db/pokemon.db"
def display_all():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM pokemon")
    data = cursor.fetchall()
    conn.close()
    return data


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

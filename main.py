import sqlite3
import os

# Nom du fichier CSV
csv_filename = 'pokemon.csv'
# Nom du fichier de la base de données SQLite
db_filename = 'pokemon.db'

# Crée une nouvelle connexion à la base de données SQLite
conn = sqlite3.connect(db_filename)
c = conn.cursor()

if not os.path.exists(db_filename):
    # Ouvre le fichier CSV
    with open(csv_filename, 'r') as f:
        # Lit la première ligne pour obtenir les noms de colonnes
        cols = f.readline().strip().split(',')

        # Crée une nouvelle table avec les noms de colonnes du fichier CSV
        c.execute("CREATE TABLE pokemon ({})".format(', '.join(cols)))

        # Lit le reste du fichier et insère les données dans la table
        for line in f:
            vals = line.strip().split(',')
            c.execute("INSERT INTO pokemon VALUES ({})".format(', '.join(['?']*len(cols))), vals)

    # Valide les modifications
    conn.commit()

def main():
    while True:
        print("1. Chercher un Pokemon")
        print("2. Ajouter un Pokemon")
        print("3. Modifier un Pokemon")
        print("4. Supprimer un Pokemon")
        print("5. Quitter")
        choice = input("Choisissez une option : ")

        if choice == "1":
            search_pokemon()
        elif choice == "2":
            add_pokemon()
        elif choice == "3":
            modify_pokemon()
        elif choice == "4":
            delete_pokemon()
        elif choice == "5":
            break
        else:
            print("Choix non valide, veuillez réessayer.")

def search_pokemon():
    search_term = input("Entrez le terme de recherche : ")

    # Obtenez les noms de toutes les colonnes
    c.execute("PRAGMA table_info(pokemon)")
    columns = [row[1] for row in c.fetchall()]

    # Construisez la requête SQL
    query = "SELECT * FROM pokemon WHERE"
    params = []

    if search_term:
        for i, column in enumerate(columns):
            if i > 0:  # Ajoutez OR avant chaque condition sauf la première
                query += " OR"
            query += f" {column} LIKE ?"
            params.append(f"%{search_term}%")

    # Exécutez la requête et affichez les résultats
    c.execute(query, params)
    results = c.fetchall()

    if results:
        print("Résultats de la recherche :")
        for result in results:
            print(result)
    else:
        print("Aucun résultat trouvé.")

def add_pokemon():
    # Obtenez les noms de toutes les colonnes
    c.execute("PRAGMA table_info(pokemon)")
    columns = [row[1] for row in c.fetchall()]

    # Demandez à l'utilisateur de saisir une valeur pour chaque colonne
    values = []
    for column in columns:
        value = input(f"Entrez {column} : ")
        values.append(value)

    # Construisez la requête SQL
    query = f"INSERT INTO pokemon ({', '.join(columns)}) VALUES ({', '.join(['?' for _ in columns])})"

    # Exécutez la requête
    c.execute(query, values)
    conn.commit()

    print("Pokemon ajouté avec succès!")

def modify_pokemon():
    # Obtenez le nom du Pokémon à modifier
    name = input("Entrez le nom du Pokemon à modifier : ")

    # Obtenez les noms de toutes les colonnes
    c.execute("PRAGMA table_info(pokemon)")
    columns = [row[1] for row in c.fetchall()]

    # Demandez à l'utilisateur de saisir une nouvelle valeur pour chaque colonne
    set_clauses = []
    values = []
    for column in columns:
        value = input(f"Entrez la nouvelle valeur pour {column} (laissez vide pour ne pas modifier) : ")
        if value != "":
            set_clauses.append(f"{column} = ?")
            values.append(value)

    # Construisez la requête SQL
    query = f"UPDATE pokemon SET {', '.join(set_clauses)} WHERE Name = ?"

    # Ajoutez le nom du Pokémon à la fin des valeurs
    values.append(name)

    # Exécutez la requête
    c.execute(query, values)
    conn.commit()

    print("Pokemon modifié avec succès!")

def delete_pokemon():
    name = input("Entrez le nom du Pokemon à supprimer : ")
    c.execute("DELETE FROM pokemon WHERE Name=?", (name,))
    conn.commit()
    print("Pokemon supprimé avec succès!")

if __name__ == "__main__":
    main()
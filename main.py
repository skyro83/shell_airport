from term_menu.menu import TerminalMenu
import db.convert
import db.function

def main():
    db_file = './db/pokemon.db'
    options = ["Rechercher", "Afficher", "Modifier", "Quitter"]
    menu = TerminalMenu(options)
    menu_entry_index = menu.show()

    # Si l'utilisateur a choisir de quitter
    if menu_entry_index == len(options) - 1:
        print("Au revoir")
        return

    # Si l'utilisateur a choisir d'afficher
    elif options[menu_entry_index] == "Afficher":
        # Récupérer toutes les tables de la base de données
        tables = db.function.get_tables(db_file)
        # Afficher les tables dans un menu
        table_menu = TerminalMenu([table[0] for table in tables])
        selected_table_index = table_menu.show()
        selected_table_name = tables[selected_table_index][0]
        # Récupérer les données de la table sélectionnée
        table_data = db.function.get_table_data(db_file, selected_table_name)
        # Afficher les données de la table
        for row in table_data:
            print(row)

    # Si l'utilisateur a choisir de rechercher
    elif options[menu_entry_index] == "Rechercher":
        # Récupérer toutes les tables de la base de données
        tables = db.function.get_tables(db_file)
        # Afficher les tables dans un menu
        table_menu = TerminalMenu([table[0] for table in tables])
        selected_table_index = table_menu.show()
        selected_table_name = tables[selected_table_index][0]
        # Demander à l'utilisateur d'entrer une valeur à rechercher
        value = input("Entrez une valeur à rechercher : ")
        # Rechercher les lignes qui contiennent cette valeur
        results = db.function.recherche(db_file, selected_table_name, value)
        # Afficher les résultats
        for row in results:
            print(row)
    elif options[menu_entry_index] == "Modifier":
        # Afficher un sous-menu avec les options de modification
        modify_options = ["Ajouter une ligne", "Supprimer une ligne", "Modifier une ligne", "Ajouter une table à partir d'un CSV"]
        modify_menu = TerminalMenu(modify_options)
        modify_option_index = modify_menu.show()

        # Si l'utilisateur a choisi d'ajouter une ligne
        if modify_options[modify_option_index] == "Ajouter une ligne":
            # Demander à l'utilisateur d'entrer les données de la nouvelle ligne
            new_row_data = input("Entrez les données de la nouvelle ligne, séparées par des virgules : ").split(',')
            # Ajouter la nouvelle ligne à la table
            db.function.add_row(db_file, selected_table_name, new_row_data)

        # Si l'utilisateur a choisi de supprimer une ligne
        elif modify_options[modify_option_index] == "Supprimer une ligne":
            # Demander à l'utilisateur d'entrer l'ID de la ligne à supprimer
            row_id = input("Entrez l'ID de la ligne à supprimer : ")
            # Supprimer la ligne de la table
            db.function.delete_row(db_file, selected_table_name, row_id)

        # Si l'utilisateur a choisi de modifier une ligne
        elif modify_options[modify_option_index] == "Modifier une ligne":
            # Demander à l'utilisateur d'entrer l'ID de la ligne à modifier et les nouvelles données
            row_id = input("Entrez l'ID de la ligne à modifier : ")
            new_row_data = input("Entrez les nouvelles données pour cette ligne, séparées par des virgules : ").split(',')
            # Modifier la ligne dans la table
            db.function.update_row(db_file, selected_table_name, row_id, new_row_data)

        # Si l'utilisateur a choisi d'ajouter une table à partir d'un CSV
        elif modify_options[modify_option_index] == "Ajouter une table à partir d'un CSV":
            # Demander à l'utilisateur d'entrer le chemin du fichier CSV
            csv_file_path = input("Entrez le chemin du fichier CSV : ")
            # Ajouter une table à la base de données à partir du fichier CSV
            db.convert.create_table(db_file, csv_file_path)

if __name__ == "__main__":
    main()
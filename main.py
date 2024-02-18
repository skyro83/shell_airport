from term_menu.menu import TerminalMenu
import db.convert
import db.function

def main():
    options = ["Rechercher", "Tout afficher", "Modifier", "Quitter"]
    menu = TerminalMenu(options)
    menu_entry_index = menu.show()
    # Si l'utilisateur a choisir de quitter
    if menu_entry_index == len(options) - 1:
        print("Au revoir")
        return

if __name__ == "__main__":
    main()
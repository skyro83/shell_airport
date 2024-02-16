from term_menu.menu import TerminalMenu

def main():
    options = ["Rechercher", "Tout afficher", "Modifier", "Quitter"]
    menu = TerminalMenu(options)
    menu_entry_index = menu.show()
    print(f"Selected option: {options[menu_entry_index]}")

if __name__ == "__main__":
    main()
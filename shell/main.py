import os
import keyboard

# Liste des options du menu
menu = ['Option 1', 'Option 2', 'Option 3', 'Quitter']

# Index de l'option actuellement sélectionnée
current_option = 0

def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, option in enumerate(menu):
        if i == current_option:
            print(f'> {option} <')
        else:
            print(option)

def up():
    global current_option
    if current_option > 0:
        current_option -= 1
    display_menu()

def down():
    global current_option
    if current_option < len(menu) - 1:
        current_option += 1
    display_menu()

keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)

# Afficher le menu pour la première fois
display_menu()

# Boucle principale
while True:
    if keyboard.is_pressed('enter'):
        if current_option == len(menu) - 1:
            break
        else:
            print(f'Vous avez sélectionné {menu[current_option]}')
            break
import keyboard
import os

class SelectMenu:
    def __init__(self, options):
        self.options = options
        self.selected = 0

    def display(self):
        os.system('clear')  # Pour Linux/OS X
        # os.system('cls')  # Pour Windows
        for index, option in enumerate(self.options):
            prefix = '>>' if index == self.selected else ''
            print(f"{prefix} {index + 1}. {option}")

    def up(self, e):
        if self.selected > 0:
            self.selected -= 1
        self.display()

    def down(self, e):
        if self.selected < len(self.options) - 1:
            self.selected += 1
        self.display()
'''
menu = SelectMenu(["Option 1", "Option 2", "Option 3"])
menu.display()
keyboard.on_press_key('up', menu.up)
keyboard.on_press_key('down', menu.down)
keyboard.wait('esc')  # Attendez que l'utilisateur appuie sur 'esc' pour quitter
'''

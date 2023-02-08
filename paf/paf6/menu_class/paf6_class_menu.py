# ------------------
# Console Menu class
# ------------------

class ConsoleMenu:
    menu = {
        '1': 'List all cars',
        '2': 'Add a car',
        '3': 'Find a car by speed parameters',
        '4': 'Count the expenses',
        '5': 'Sort all cars by fuel consumption',
        '6': 'Exit'
    }

    def print_menu(self):
        print('\nWelcome to Taxi Station! Please choose your option:')
        for i in self.menu:
            print(f'\t{i}. {self.menu[i]}')

    def choose_from_menu(self):
        while True:
            self.print_menu()
            option = input('--> ')
            if option in self.menu:
                return option
            else:
                print("Such option does not exist.")

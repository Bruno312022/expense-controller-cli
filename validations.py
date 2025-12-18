def read_expense_input():
    while True:
        try:
            value = float(input("Enter expense value: "))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Invalid value. Enter a positive number")

def read_option_input():
    while True:
        try:
            option = int(input("Choose an operation: "))
            if option < 0:
                raise ValueError
            return option
        except ValueError:
            print("Invalid option. Enter a number displayed on the menu")


def read_ask_client():
    while True:
        try:
            ask_client = input("Clear all? (y/n) ").lower()

            if ask_client != "y" and ask_client != "n":
                raise ValueError
            return ask_client
        except ValueError:
            print("Only (y) or (n) allowed")
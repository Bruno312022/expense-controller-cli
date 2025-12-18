import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

from expenses import (
    register_expenses,
    total_expenses,
    clear_expenses,
    list_expenses,
    highest_and_lowest_expense
)

from validations import (
    read_option_input,
    read_expense_input,
    read_ask_client
)

expenses = []

while True:
    print("\n=== EXPENSE TRACKER ===")
    print("1 - Register expense")
    print("2 - List expenses")
    print("3 - Total expenses")
    print("4 - Highest and lowest expense")
    print("5 - Clear expenses")
    print("0 - Exit")

    option = read_option_input()
    if option == 1:
        value = read_expense_input()
        register_expenses(expenses, value)
        clear_screen()
        print("Expense added.")
        

    elif option == 2:
        result = list_expenses(expenses)
        if result is None:
            clear_screen()
            print("No expenses.")
        else:
            clear_screen()
            print(result)

    elif option == 3:
        total = total_expenses(expenses)
        if total is None:
            clear_screen()
            print("No expenses.")
        else:
            clear_screen()
            print("Total:", total)

    elif option == 4:
        result = highest_and_lowest_expense(expenses)
        if result is None:
            clear_screen()
            print("No expenses.")
        else:
            highest, lowest = result
            clear_screen()
            print("Highest:", highest)
            print("Lowest:", lowest)

    elif option == 5:
        ask_client = read_ask_client()
        if ask_client == "y":
            clear_expenses(expenses)
            clear_screen()
            print("Expenses cleared.")
        else:
            clear_screen()
            print("aborting operation")

    elif option == 0:
        print("Bye.")
        break
    else:
        print("Invalid option.")

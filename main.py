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

from cli_ui import (
    header,
    pause,
    show_menu
)

expenses = []

while True:
    header("EXPENSE TRACKER")
    show_menu()

    option = read_option_input()

    if option == 1:
        header("REGISTER EXPENSE")
        value = read_expense_input()
        register_expenses(expenses, value)
        print("\nExpense added successfully.")
        pause()

    elif option == 2:
        header("LIST EXPENSES")
        result = list_expenses(expenses)
        if result is None:
            print("No expenses registered.")
        else:
            for i, expense in enumerate(result, start=1):
                print(f"{i}. ${expense:.2f}")
        pause()

    elif option == 3:
        header("TOTAL EXPENSES")
        total = total_expenses(expenses)
        if total is None:
            print("No expenses registered.")
        else:
            print(f"Total: ${total:.2f}")
        pause()

    elif option == 4:
        header("HIGHEST AND LOWEST")
        result = highest_and_lowest_expense(expenses)
        if result is None:
            print("No expenses registered.")
        else:
            highest, lowest = result
            print(f"Highest: ${highest:.2f}")
            print(f"Lowest : ${lowest:.2f}")
        pause()

    elif option == 5:
        header("CLEAR EXPENSES")
        ask_client = read_ask_client()
        if ask_client == "y":
            clear_expenses(expenses)
            print("All expenses cleared.")
        else:
            print("Operation cancelled.")
        pause()

    elif option == 0:
        header("EXIT")
        print("Bye.")
        break

    else:
        print("Invalid option.")
        pause()
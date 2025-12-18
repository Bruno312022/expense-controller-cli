from expenses import (
    register_expenses,
    total_expenses,
    clear_expenses,
    list_expenses,
    highest_and_lowest_expense
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

    option = input("Choose an option: ")

    if option == "1":
        value = float(input("Enter expense value: "))
        register_expenses(expenses, value)
        print("Expense added.")

    elif option == "2":
        result = list_expenses(expenses)
        if result is None:
            print("No expenses.")
        else:
            print(result)

    elif option == "3":
        total = total_expenses(expenses)
        if total is None:
            print("No expenses.")
        else:
            print("Total:", total)

    elif option == "4":
        result = highest_and_lowest_expense(expenses)
        if result is None:
            print("No expenses.")
        else:
            highest, lowest = result
            print("Highest:", highest)
            print("Lowest:", lowest)

    elif option == "5":
        clear_expenses(expenses)
        print("Expenses cleared.")

    elif option == "0":
        print("Bye.")
        break

    else:
        print("Invalid option.")

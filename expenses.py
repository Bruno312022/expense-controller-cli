def register_expenses(expenses, item):
    expenses.append(item)

def is_empty(expenses):
    return len(expenses) == 0


def total_expenses(expenses):
    if is_empty(expenses):
        return None
    total = 0
    for expense in expenses:
        total += expense
    return total


def clear_expenses(expenses):
    if is_empty(expenses):
        return None
    expenses.clear()


def list_expenses(expenses):
    if is_empty(expenses):
        return None
    return expenses


def highest_and_lowest_expense(expenses):
    

    if is_empty(expenses):
        return None
    
    highest = expenses[0]
    lowest = expenses[0]
    for expense in expenses:
        if expense > highest:
            highest = expense

        if expense < lowest:
            lowest = expense

    return highest, lowest






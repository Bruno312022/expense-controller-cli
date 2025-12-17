def register_expenses(expenses, item):
    expenses.append(item) 

def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense
    return total

def list_expenses(expenses):
    if is_empty(expenses):
        return None
    return expenses

def is_empty(expenses):
    if len(expenses) == 0:
        print("no expenses")


expenses = []





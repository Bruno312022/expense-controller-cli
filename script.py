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

# ===== MANUAL TESTS =====

print("=== TEST 1: EMPTY LIST ===")
expenses = []

print("is_empty:", is_empty(expenses))                  # Expected: True
print("total_expenses:", total_expenses(expenses))      # Expected: None
print("list_expenses:", list_expenses(expenses))        # Expected: None
print("highest_and_lowest:", highest_and_lowest_expense(expenses))  # Expected: None
clear_expenses(expenses)
print("after clear:", expenses)                          # Expected: []


print("\n=== TEST 2: SINGLE EXPENSE ===")
expenses = []
register_expenses(expenses, 100.0)

print("expenses:", expenses)                             # Expected: [100.0]
print("is_empty:", is_empty(expenses))                   # Expected: False
print("total_expenses:", total_expenses(expenses))       # Expected: 100.0
print("list_expenses:", list_expenses(expenses))         # Expected: [100.0]
print("highest_and_lowest:", highest_and_lowest_expense(expenses))  # Expected: (100.0, 100.0)


print("\n=== TEST 3: MULTIPLE EXPENSES ===")
expenses = []
register_expenses(expenses, 200.0)
register_expenses(expenses, 50.0)
register_expenses(expenses, 300.0)

print("expenses:", expenses)                             # Expected: [200.0, 50.0, 300.0]
print("total_expenses:", total_expenses(expenses))       # Expected: 550.0
print("highest_and_lowest:", highest_and_lowest_expense(expenses))  # Expected: (300.0, 50.0)


print("\n=== TEST 4: CLEAR AND REUSE ===")
clear_expenses(expenses)
print("after clear:", expenses)                          # Expected: []

register_expenses(expenses, 75.0)
print("expenses:", expenses)                             # Expected: [75.0]
print("total_expenses:", total_expenses(expenses))       # Expected: 75.0
print("highest_and_lowest:", highest_and_lowest_expense(expenses))  # Expected: (75.0, 75.0)

print("\n=== ALL MANUAL TESTS FINISHED ===")




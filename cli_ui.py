import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def header(title):
    clear_screen()
    print("=" * 30)
    print(title.center(30))
    print("=" * 30)


def show_menu():
    print("1 - Register expense")
    print("2 - List expenses")
    print("3 - Total expenses")
    print("4 - Highest and lowest expense")
    print("5 - Clear expenses")
    print("0 - Exit")
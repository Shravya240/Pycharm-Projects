"""
Project Goal:
-------------
    Level 1:
        A. Create a text-based application that manages a shopping list using a list.
        B. Allow users to add new items, remove items, and view the current list.
    Level 2:
        In next Class
"""

# Operators : Aritmetic , Comparison, Logical(AND,OR,NOT), Membership (IN,Not In), Identity  (Is , Is not), Bitwise Operators
# Control Structure/Flow: Sequence, selection, Repetition (While, For)

shopping_lists = []


def add_items_in_lists(number_of_items):  # 5
    for i in range(number_of_items + 1):
        items = input("What would you like to add: ")
        shopping_lists.append(items)

    print(f"List:{shopping_lists}")  # Debug


def remove_items_in_lists(items):
    if items in shopping_lists:
        shopping_lists.remove(items)
        print(f" Items is removed successfully. List:{shopping_lists}")  # Debug
    else:
        print(f" Items is not there. List:{shopping_lists}")  # Debug


def view_list():
    print(f"List:{shopping_lists}")


def Main_ShoppingListApp():
    while True:
        print("Welcome to Shopping App")
        print("1. Create a List: ")
        print("2. Add Items in a list:")
        print("3. Remove Items in a list: ")
        print("4. View the Items in a List: ")
        print("5. Exit")

        options = int(input("What you like to do ? "))

        if options == 1:
            list_name = input("Enter list name: ")
        elif options == 2:
            num_items = input(f"How many items you like to add {list_name}: ")
            add_items_in_lists(int(num_items))
        elif options == 3:
            items = input(f"What would you like to remove from {list_name}: ")
            remove_items_in_lists(items)
        elif options == 4:
            view_list()
        elif options == 5:
            print("Lists is there. Thank you")
            break


Main_ShoppingListApp()
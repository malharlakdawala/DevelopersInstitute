import Exc1
from Exc1 import MenuItem


# def load_manager():
#     self.

def show_user_menu():
    user_input = input("""
    a-> Add an item
    d-> Delete an Item
    v-> View the menu
    x-> Exit    
    """)
    if user_input == "a":
        add_item_to_menu()
    elif user_input == "d":
        remove_item_from_menu()
    elif user_input == "v":
        show_all()
    elif user_input == "x":
        exit()
    else:
        print("wrong input")
        return show_user_menu()


def add_item_to_menu():
    item_name = input("Enter name of item to input: ")
    item_price = int(input("Enter name of item to input: "))
    item.save(item_name, item_price)
    show_user_menu()


def remove_item_from_menu():
    item_name = input("Enter name of item to delete: ")
    item.delete(item_name)
    show_user_menu()

def show_all():
    item.all()
    show_user_menu()

item = MenuItem()
show_user_menu()

from Exc2menu_manager import MenuManager

def load_manager(menu2):
    pass
def show_user_menu():
    menu_input = input('''
    MENU:
    a-> Add a Item
    b-> Delete an Item
    c-> View the Menu
    x-> Exit 
    ''')
    if menu_input == "a": add_item_to_menu()
    elif menu_input == "b": remove_item_from_menu()
    elif menu_input == "c": show_restaurant_menu()
    elif menu_input == "x": exit()

def add_item_to_menu():
    name_item_to_add = input("please enter name of item to add: ")
    price_item_to_add = int(input("please enter price of item to add: "))
    menu2 = MenuManager()
    menu2.add_item(name_item_to_add,price_item_to_add)
    menu2.save_to_file()
    show_user_menu()

def remove_item_from_menu():
    name_item_to_remove = input("please enter name of item to add: ")
    menu2 = MenuManager()
    menu2.remove_item(name_item_to_remove)
    menu2.save_to_file()
    show_user_menu()

def show_restaurant_menu():
    menu2 = MenuManager()
    menu2.show_menu()
    show_user_menu()

show_user_menu()






from menu_item import MenuItem

def show_user_menu():
    choose = input("A)Add an Item\n D) Delete an Item \n V) Delete an Item \nX)Exit \n").upper()
    return choose

def add_an_item():
    new_item = input ("Add an item")
    new_price= int(input("Add price"))
    new_one= MenuItem(new_item, new_price)
    return new_one
    print("Item was added successfully.")


def remove_item_from_menu():
    new_item = input ("What item would you like to delete")
    new_delete= MenuItem.delete(new_item)
    print("Item was deleted successfully.")


def main():
    choice = show_user_menu()
    while choice != "X":
        if choice == "A":
             add_an_item()
        #    return add
        elif choice == "D":
            remove = remove_item_from_menu()
            return remove
        elif choice == "V":
            print(MenuItem.all())
    print(MenuItem.all())
    return

def load_manager():
    menu=MenuItem("Fries", 5)


main()
load_manager()

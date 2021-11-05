#run this file, first menu option, can add p, s, x
# and for game, type "rock", "paper", 'scissor'
from Game import Game

a = {"win": 0, "draw": 0, "loss": 0}


def get_user_menu_choice():
    user_menu_choice = input("""
    MENU:
    p-> Play a New Game
    s-> Show scores
    x-> Quit    
    """)
    if user_menu_choice == "p" or user_menu_choice == "s" or user_menu_choice == "x":
        return user_menu_choice
    else:
        print("Enter either of p, s or x ")
        return get_user_menu_choice()


def print_results():
    print("The score is: ", a)


def main():
    while True:
        user_menu_choice = get_user_menu_choice()
        if user_menu_choice == "p":
            result = Game().play()
            if result in a:
                a[result] += 1
            print_results()
        elif user_menu_choice == "s":
            print_results()
        elif user_menu_choice == "x":
            print_results()
            exit()
        else:
            print("Incorrect Input, please try again ")

main()

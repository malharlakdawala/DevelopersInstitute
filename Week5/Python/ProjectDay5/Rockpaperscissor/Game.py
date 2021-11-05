import random


class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        self.user_item = input("""
        Select your weapon:
        rock
        paper
        scissor
        """)
        if self.user_item == "rock" or self.user_item == "paper" or self.user_item == "scissor":
            return self.user_item
        else:
            print("Enter either of these 'rock', 'paper' or 'scissor' ")
            return self.get_user_item()

    def get_computer_item(self):
        self.computer_item = random.choice(["rock", "paper", "scissor"])
        return self.computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == "rock" and computer_item == "scissor":
            return "win"
        elif user_item == "scissor" and computer_item == "paper":
            return "win"
        elif user_item == "paper" and computer_item == "rock":
            return "win"
        elif user_item == computer_item:
            return "draw"
        else:
            return "loss"

    def play(self):
        user_item=self.get_user_item()
        computer_item=self.get_computer_item()
        result=self.get_game_result(user_item,computer_item)
        print(f"You selected '{user_item.upper()}', computer selected '{computer_item.upper()}', the result is '{result.upper()}'")
        return result



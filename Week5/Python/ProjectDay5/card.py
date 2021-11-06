import random


class Card:
    def __init__(self):
        card_num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        card_type = ["Heart", "Diamond", "Club", "Spade"]
        self.a = [[v + ' of ' + s] for s in card_type for v in card_num]
        self.black_list=[]

    def deal(self):
        while True:
            d = random.randint(0, 51)
            if d not in self.black_list:
                print(self.a[d])
                self.black_list.append(d)
                print("black list: ",len(self.black_list))
                print("cards in deck: ",len(self.a))
                break

a=Card()
for i in range(45):
    a.deal()

# def deal

# create an array of cards in init, for deal, select random number between 0 to 51
# create a blacklist, which holds all random no. generated, check if new random no. is not
# there in blacklist, if true, then print value at that index, append that no. in blacklist

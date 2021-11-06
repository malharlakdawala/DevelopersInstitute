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
for i in range(55):
    a.deal()

# def deal
# from above array, do random [i][j], show value at ij, store i,j in black list, next time compare new i,j pair with blacklist, allow only positive ones/

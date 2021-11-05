import json
import random


class Character:
    def __init__(self):
        self.stregnth = self.no_assign()
        self.dexterity = self.no_assign()
        self.constitution = self.no_assign()
        self.intelligence = self.no_assign()
        self.wisdom = self.no_assign()
        self.charisma = self.no_assign()

    def no_assign(self):
        a = sorted([random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)])
        return a[1] + a[2] + a[3]

class Game:
    def __init__(self, num):
        self.num = num
        self.generate_characters(num)
        self.make_json_file()

    def generate_characters(self, num):
        self.a = []
        for i in range(num):
            name = input(f"enter name of character {i + 1}: ")
            age = input(f"enter age of character {i + 1}: ")
            self.a.append(
                {"name": name, "age": age,
                 "attributes": {
                     "stregnth": Character().stregnth,
                     "dexterity": Character().dexterity,
                     "constitution":Character().constitution,
                     "intelligence": Character().intelligence,
                     "wisdom":Character().wisdom,
                     "charisma":Character().charisma
                 }})  # add attributes here
        print(self.a)

    def make_json_file(self):
        json_obj=json.dumps(self.a,indent=2)
        with open("characters.json","w") as file:
            file.write(json_obj)



num = int(input("How many characters you want? "))
game1 = Game(num)


# {
# name:"malhar",
# age: 25,
# attributes:{
#
#     stregnth:15,
#     stregnth:15,
#     stregnth:15,
#     stregnth:15,
#     stregnth:15,
# }
# }


# def generate_characters(num):
#     a=[]
#     for i in range(num):
#         name=input(f"enter name of character {i+1}: ")
#         age=input(f"enter age of character {i+1}: ")
#         a.append()
#
#     return (name,age)

chr1 = Character()

# Exercise 1 : Family
import random


class Family:
    def __init__(self,members,last_name):
        self.members=members
        self.last_name=last_name

    def born(self,**kwargs):
        self.members.append(kwargs)

    def is_18(self,name):
        self.namechk=name
        for i in self.members:
            if self.namechk == i["name"]:
                if i["age"]>18: return True
                else: return False

    def print_all(self):
        print(self.members)


#Exercise 2 : TheIncredibles Family
class TheIncredibles(Family):
    def __init__(self,members,last_name):
        super().__init__(members,last_name)
        powers = ["super-strength","elasticity","invisbility","electromagnetic field", "Jack Attack"]
        for character in self.members:
            character["power"]=powers[random.randint(0,4)]

    def use_power(self):
        for i in self.members:
            if i["age"]>18: print(i["power"])



      #  print([char["age"] in char for char in self.members] if char["age"]>18)

family1 = TheIncredibles([
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':12,'gender':'Female','is_child':False}
], "Johnson")

family1.born(name='Baby Jack',age=3,gender='Male',is_child=True)

family1.use_power()

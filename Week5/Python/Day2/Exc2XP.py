# Exercise 1 : Family
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
        pass

family1 = Family([
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':12,'gender':'Female','is_child':False}
], "Johnson")

#a = {'name':'Michael','age':35,'gender':'Male','is_child':True}
family1.born(name='Michael',age=35,gender='Male',is_child=True)

print(family1.is_18("Sarah"))

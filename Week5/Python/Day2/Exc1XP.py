#
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Bread(Cat):
#     pass
#
# cat1 = Cat("Syphonie",5)
# cat2 = Cat("Ronnie",8)
# cat3 = Cat("Tribianie",9)
#
# my_cats = [cat1,cat2, cat3]
#
# my_pets = Pets(my_cats)
# my_pets.walk()
#
# Exercise 2 : Dogs
import random


class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age * 10)

    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            print(f"{self.name} is the winner as his product is {self.run_speed()}*{self.weight}")
        else:
            print(f"{other_dog.name} is the winner as his product is {other_dog.run_speed()}*{other_dog.weight}")


charlie = Dog("charlie", 5, 12)
jasper = Dog("jasper", 8, 10)
oscar = Dog("oscar", 11, 15)


# print(oscar.bark())
# print(jasper.run_speed())
# jasper.fight(oscar)
# oscar.fight(jasper)
# jasper.fight(charlie)

# Exercise 3 : Dogs Domesticated

class Petdog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)

        self.trained = False

    def train(self):
        self.trained = True
        print(self.bark())

    def play(self, *args):
        print(f"{self.name}, {self.args} all play together ")

    def do_a_trick(self):
        random_print_list = [f"{self.name} does a barell roll", f"{self.name} does stands on his back legs",
                             f"{self.name} shakes your hand", f"{self.name} plays dead"]
        if self._trained:
            print(random_print_list[random.randint(0, 3)])


rex = Petdog("rex", 5, 12)
rex.train()

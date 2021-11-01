# class Shape:
#   sides = 4 #first property
#   name = "Square" #second property
#   def description(a): #method defined
#     return ("A square with 4 sides")
#
# s1 = Shape() #creating an object of Shape
# print "Name of shape is:",(s1.name)
# print "Number of sides are:",(s1.sides)
# print s1.description()


# class Animal():
#   def __init__(self, type, number_legs, sound):
#     self.type = type
#     self.number_legs = number_legs
#     self.sound = sound
#
#   def make_sound(self):
#     print(f"I am an animal, and I love saying {self.sound}")
#
#
# class Dog(Animal):
#   pass
#
# rex= Dog("dog", 4, "wouaf")
# print('This animal is a:', rex.type)
# print('This dog makes the sound ', rex.sound)
# rex.make_sound()


# class Parrot():
#
#   def fly(self):
#     print("Parrot can fly")
#
#   def swim(self):
#     print("Parrot can't swim")
#
#
# class Penguin():
#
#   def fly(self):
#     print("Penguin can't fly")
#
#   def swim(self):
#     print("Penguin can swim")
#
#
# # common interface
# def flying_test(bird):
#   bird.fly()
#
# blu = Parrot()
# peggy = Penguin()
#
# flying_test(blu)
# flying_test(peggy)

# class Alien():
#     def __init__(self, name, planet):
#         self.name = name
#         self.planet = planet
#
#     def fly(self):
#         print(self.name, 'is flying!')
#
#     def sleep(self):
#         print("Aliens don't sleep")
#
#
# class Animal():
#     def __init__(self, name):
#         self.name = name
#
#     def sleep(self):
#         print("zzzZZZZZ")
#
#     def sleep1(self):
#         print("sleeping aramse")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("{} barked, WAF !".format(self.name))
#
#
# class AlienDog(Alien, Dog):
#     def bark(self):
#         print("{} barked, 0ul10ul0u (that's how aliens dogs bark..) !".format(self.name))
#
#
# my_normal_dog = Dog("Roger")
# my_alien_dog = AlienDog("Rex", "Neptune")
# print(my_alien_dog.planet)
#
# my_alien_dog.fly()
# my_alien_dog.sleep()
# my_alien_dog.bark()
# my_alien_dog.sleep1()
#

# class Book():
#     def __init__(self, title, author, publication_date, price):
#         self.title = title
#         self.author = author
#         self.publication = publication_date
#         self.price = price
#
#     def present(self):
#         print(f'Title: {self.title}')
#
# class Fiction(Book):
#     def __init__(self, title, author, publication_date, price, is_awesome):
#         super().__init__(title, author, publication_date, price)
#         self.genre = 'Fiction'
#         self.is_awesome = is_awesome
#         if self.is_awesome:
#             self.bored = False
#             print('Woow this is an awesome book')
#         else:
#             self.bored = True
#             print('I am very bored')
#
# if __name__ == '__main__':
#     foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
#     foundation.present()
#     print(foundation.price)
#     print(foundation.bored)
#     boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
#     print(boring_book.bored)

#wow this is an awesome book
#title asimov
#5
#false
#i am very bored
#true




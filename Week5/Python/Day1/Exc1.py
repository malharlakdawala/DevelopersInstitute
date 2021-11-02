# import copy
#
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# def calc_max_age(*args):
#     temp_age=0
#     catMax = copy.copy(args[0]) #assigning first object to temp
#     for i in range(len(args)):
#         if args[i].age>temp_age:
#             temp_age=args[i].age
#             catMax = copy.copy(args[i])  #assigning larg object to temp
#     return catMax  #returning temp max object
#
#
# cat1 = Cat("Tommy", 5)
# cat2 = Cat("Shera", 8)
# cat3 = Cat("Tiger", 10)
#
# catMax1 = calc_max_age(cat1,cat2,cat3)  #fetching the object object
# print(catMax1.name,catMax1.age)

#Exercise 2 : Dogs

# class dog:
#     def __init__(self,name,height):
#         self.name=name
#         self.height=height
#
#     def bark(self):
#         print(f'{self.name} goes woof!')
#
#     def jump(self):
#         print(f'{self.name} jumps {self.height*2} cm high')
#
# davis_dog = dog("Rex",50)
# davis_dog.bark()
# davis_dog.jump()
#
# sarahs_dog = dog("Teacup",20)
# sarahs_dog.bark()
# sarahs_dog.jump()
#
# if davis_dog.height>sarahs_dog.height:
#     print(f'{davis_dog.name} is tall')
# else: print(f'{sarahs_dog.name} is tall')
#
#
# Exercise 3 : Who’s The Song Producer?

# class song:
#     def __init__(self,lyrics):
#         song.lyrics=lyrics
#     def sing_me_a_song(self):
#         for i in range(len(self.lyrics)):
#             print(self.lyrics[i])
# stairway= song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()
#
# Exercise 4 : Afternoon At The Zoo

# class zoo:
#     def __init__(self,zoo_name):
#         self.name = zoo_name
#         self.animals=[]
#
#     def add_animal(self, new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)
#
#     def get_animals(self):
#         print(*self.animals)
#
#     def sell_animal(self,animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)
#
#     # def sort_animals(self):
#     #     self.animals.sort()
#     #     for val, k in self.animals:
#     #         print(k)
#     #
#     def sort_animals(self):
#         groups=defaultdict(list)
#         for animal in self.animals:
#             groups[animal[0]].append(animal)
#         animal_sorted = sorted(groups.values())
#         self.index_animal = {}
#         for index, animal in enumerate(animal_sorted):
#             self.index_animal[index+1]=animal
#
#
#
#
# mumbai_zoo = zoo("Mumbai Zoo")
# mumbai_zoo.add_animal("peacock")
# mumbai_zoo.add_animal("lion")
# mumbai_zoo.add_animal("ape")
# mumbai_zoo.add_animal("baboon")
# mumbai_zoo.add_animal("bear")
# mumbai_zoo.add_animal("cat")
# mumbai_zoo.add_animal("cougar")
#
# mumbai_zoo.get_animals()
# mumbai_zoo.sort_animals()
# mumbai_zoo.get_animals()


class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        '''This method adds the new_animal
        to the animals list as long as it isn't already in the list.'''
        if not new_animal in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        '''prints all the animals of the zoo.'''
        for animal in self.animals:
            print(animal)

    def sell_animal(self, animal_sold):
        '''removes the animal from the list if it exists in the list.'''
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        '''Create a method called sort_animals that sorts the animals
         alphabetically and groups them together based on their first letter.'''
        animals_lists = []
        for animal in sorted(self.animals):
            print('current animal:', animal)
            if not animals_lists:
                animals_lists.append([animal])

            else:
                # print(f"current animal first letter: {animal[0]}")
                # print(f"last list: {animals_lists[-1]}")
                # print(f"first object in last list: {animals_lists[-1][0]}")
                # print(f"first letter of first object in last list: {animals_lists[-1][0][0]}")
                if animal[0] == animals_lists[-1][0][0]:
                    # print('matches last object')
                    animals_lists[-1].append(animal)
                else:
                    animals_lists.append([animal])

            print(animals_lists)


ramat_gan_safari = Zoo('Ramat Gan Safari')
for animal in ['Cat', 'Cougar', "Baboon", 'Eel', 'Emu', "Baboon", "Baboon", "Baboon", "Bear", "Ape", ]:
    ramat_gan_safari.add_animal(animal)

ramat_gan_safari.sort_animals()


# need help with below. list to dictionary conversion?
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example
#
# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }



# class Dog():
#     def __init__(self, my_color, my_height):
#         self.legs = 4
#         self.color = my_color
#         self.height = my_height
#
#     def introduce(self):
#         print(f'this dog has {self.legs}, is the color {self.color}, and is {self.height}m tall')
#
# dog1 = Dog('red', 1.56)
# print(dog1)
# dog1.introduce()
# dog2 = Dog('blue', 0.43)
# print(dog2)
# dog2.introduce()
#
#
# class Dog():
#     # Initializer / Instance Attributes
#     def __init__(self, name_of_the_dog):
#         print("A new dog has been initialized !")
#         print("His name is", name_of_the_dog)
#         self.name = name_of_the_dog
#
#     def bark(self):
#         print(f"{self.name} barks ! WAF")
#
#     def walk(self, number_of_meters):
#         print(f"{self.name} walked {number_of_meters} meters")
#
#     def rename(self, new_name):
#         self.name = new_name
#
#
# dog1 = Dog('Rex')
# print(dog1.name)
# dog1.bark()
# dog1.walk('100')
# dog1.rename('Sparky')
#
#
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# def oldest_cat(cat_list):
#     # max([cat.age for cat in cat_list])
#     return sorted(cat_list, key=lambda cat:cat.age, reverse=True)[0]
#
# def oldest_longer(cat_list):
#     age = cat_list[0].age
#     current_cat = cat_list[0]
#     for cat in cat_list:
#         if cat.age > age:
#             current_cat = cat
#     return current_cat
#
#
# data_list = [('rex', 34), ('mr bubbles', 12), ('meowscules', 8)]
# cats = [Cat(*data) for data in data_list]
# oldest = oldest_cat(cats)
# print(oldest.name, oldest.age)
# oldest = oldest_longer(cats)
# print(oldest.name, oldest.age)
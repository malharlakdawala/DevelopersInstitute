# Exercise 1 : Geometry
#
# import math
#
# class Circle:
#     def __init__(self,radius=1):
#         self.radius=radius
#
#     def area(self):
#         return self.radius**2*math.pi
#
#     def perimeter(self):
#         return self.radius*2*math.pi
#
#     def geometrical_definition(self):
#         return f'random text random text random text '
#
# circle1 = Circle(3)
# print(circle1.area())
# print(circle1.perimeter())
# print(circle1.geometrical_definition())
#
# Exercise 2 : Custom List Class
# import random
#
#
# class MyList:
#     def __init__(self,input_list):
#         self.input_list = input_list
#
#     def sorted_list(self):
#         return sorted(self.input_list)
#
#     def reverse_list(self):
#         return sorted(self.input_list, reverse=True)
#
#     def random_list(self):
#         new_list = []
#         for i in range(len(self.input_list)):
#             new_list.append(random.randint(1,10))
#         return new_list
#
# list1 = MyList([11,5,2,7,9,8,10,88,74])
# print(list1.sorted_list())
# print(list1.reverse_list())
# print(list1.random_list())
#
# Exercise 3 : Restaurant Menu Manager

class MenuManager:
    def __init__(self):
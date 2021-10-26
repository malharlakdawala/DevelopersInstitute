# 1
# my_fav_numbers = [4,5,7]
# my_fav_numbers.append(9)
# my_fav_numbers.append(10)
# print(my_fav_numbers)
#
# my_fav_numbers.pop(-1)
#
# friend_fav_numbers = [78,98,74]
#
# our_fav_numbers = my_fav_numbers+friend_fav_numbers
#
# print(our_fav_numbers)

# 2
# a = (2,3,4)

# cant concatenate

# 3
# numbers = range(1,20)
#
# for n in numbers:
#     print(n)

# 4
# numbers = range(0,10)
# a=[]
# for n in numbers:
#     a.append(1.5+n*0.5)
# print(a)

# 5
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# basket.pop(0)
# basket.pop(-1)
# basket.append("kiwi")
# basket.insert(0,"Apples")
# x=basket.count("Apples")
# basket.clear()
# print(x,basket)

# 6
# name=""
# while name!="malu":
#     name=input("enter name")

# 7
# a=[7,8,9,5,1,0,2,5,4]
# for n in range(0,len(a)):
#     if(n%2==0):
#         print(a[n])

# 8
# for n in range(1500,2500):
#     if(n%5==0 and n%7==0):
#         print(n)

# 9
# a = input("enter fruits ")
# a=a.split()
# print(a)
# b = input("enter fav fruit ")
# if b in a:
#     print("in list")
# else:
#     print("not in list")

# 10
topping = ""
a = []
while topping != "quit":
    topping = input("enter pizza topping ")
    a.append(topping)
print(a)

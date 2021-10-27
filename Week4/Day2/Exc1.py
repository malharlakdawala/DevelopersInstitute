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
# flag=0
# topping = ""
# a = []
# while flag==0:
#     topping = input("enter pizza topping ")
#     if topping!="quit":
#         print(f"pizza topping {topping} will be added in your pizza")
#         a.append(topping)
#     else:
#         break
# print(a)
# print(f"price is {10+len(a)*2.5}")

# 11
# number_of_family_members = int(input("how many family members you have? ")) #3
# a=[]
# sum=0
# c=number_of_family_members
# number_of_family_members=1
# while number_of_family_members==c:
#     b=int(input(f"Person {number_of_family_members}, please share your age? "))
#     if b<=3:
#         price=0
#     elif 3<b<=12:
#         price=10
#     else: price=15
#     sum=sum+price
#     number_of_family_members+=1
# print(f"total family members are {number_of_family_members} and their price is {sum}")

# 12  Who Is Under 16?
# a=["Vinod", "Rohan", "Malhar", "Sonakshi"]
# for n in a:
#     b=int(input(f"{n}, please tell your age? "))
#     if b<16: a.remove(n)
# print(a)

# 13
# sandwich_orders =["Vegetable Sandwich", "Grill Sandwich", "Toast Sandwich", "Cheese Sandwich"]
# finished_sandwiches=[]
# for n in sandwich_orders:
#     #do some operation, so that sandwich is made
#     print(f"{n} is made")
#     finished_sandwiches.append(n)
# print(finished_sandwiches)

# 14

sandwich_orders = ["Vegetable Sandwich", "Pastrami Sandwich", "Grill Sandwich", "Pastrami Sandwich", "Toast Sandwich",
                   "Pastrami Sandwich", "Cheese Sandwich"]
print("Pastrami Sandwich is over")
finished_sandwiches=[]
for n in sandwich_orders:
    #do some operation, so that sandwich is made
    if(n!="Pastrami Sandwich"):
        print(f"{n} is made")
        finished_sandwiches.append(n)
print(finished_sandwiches)

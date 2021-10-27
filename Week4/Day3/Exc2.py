# Exercise 1,2,3: Birthday Look-Up
# birthdays = {"Malhar":"20/11/89","Sonakshi":"30/11/90","Rohan":"23/03/93","Vaibhav":"27/08/89","Nirali":"01/05/91"}
# #print(birthdays.keys())
# new_name = input("Add new name to add in the list ")
# new_birthdate = input("Add the birthdate to add in the list ")
# birthdays[new_name]=new_birthdate
# print(birthdays)
# name=input(f'Enter name from {birthdays.keys()} ')
# if name in birthdays.keys():
#     print(f'birtdate of {name} is {birthdays[name]}')
# else:
#     print("name not in list")

# Exc 4 Fruit shop
# import random
# items = {"banana": 4,
#          "apple": 2,
#          "orange": 1.5,
#          "pear": 3
#          }
# sum=0;
# for n in items:
#     items[n]={}
#     items[n]["price"]=random.randint(1,9)
#     items[n]["stock"]=random.randint(1,9)
#     sum+=items[n]["price"]*items[n]["stock"]
# print(items)
# print(sum)

#Exercise 5 : Cars
# a = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
# a=a.split(",")
# print(f"no. of car mfg companies are  {len(a)}")
# count_o = 0
# count_not_i=0
# for n in a:
#     if "o" in n:
#         count_o= count_o+1
#     if "i" not in n:
#         count_not_i+=1
# print(count_o,count_not_i)

b =["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
b=list(set(b))
str=" "
d=" ".join(b)
print(d)
e=sorted(b)
f=[]
for n in e:
    f.append(n[::-1])
print(f)

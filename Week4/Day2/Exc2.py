# Exercise 1 : Concatenate Lists
# a = ["Green", "Blue", "Pink"]
# b = ["Red", "Orange", "Violet"]
# for n in b:
#     a.append(n)
# print(a)
#
# Exc 2: Greatest Number
# big=0
# for n in range(0,3):
#     i=int(input("Enter number "))
#     if i>big:
#         big=i
# print(f"largest number is {big}")
#
# Exercise 3 : The Alphabet
# a = "abcdefghijklmnopqrstuvwxyz"
# for n in a:
#     if(n=="a" or n=="e" or n=="i" or n=="o" or n=="u"):
#         print(f"{n} is a Vowel")
#     else: print(f"{n} is a Consonant")
#
# Exercise 4 :
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# name = input("Tera naam bol bhai? ")
# for n in names:
#     if (name==n):
#         print(f"index of {n} is {names.index(n)}")
#
# Exercise 5 : Words And Letters
# words = input("7 words ka string de ")
# words=words.split()
# letter = input("Single character diyo ")
# for nw in words:
#     for nl in nw:
#         flag=0
#         if(nl==letter):
#             print(f"letter {nl} in {nw} comes at index = {nw.index(nl)}")
#             flag = 1
#             break
#     if flag==0: print(f"letter {letter} not found in {nw} ")
#
# Ex6
# a = list(range(1,1000000))
# print(min(a),max(a),sum(a))
#
# Ex 7
# i = input("share comma seprated numbers ")
# i=i.split(",")
# i=tuple(i)
# print(i)
#
# Exercise 8 : Random Number
import random


win = 0
loose = 0
continue1 = "yes"
while continue1 == "yes":
    a = int(input("Add no. b/w 1 and 9 "))
    b = random.randint(1, 9)
    if a == b:
        print("winner")
        win += 1
    else:
        print("looser")
        loose += 1
    continue1= input("do you want to play more? yes or quit? ")
print(f"total wins are {win} and loses are {loose}")

#Exercise 1: List Of Integers - Randoms
# import random
#
# a=[]
# b=random.randint(1,50)
# while b!=0:
#     a.append(random.randint(-100,100))
#     b=b-1
#
# print(a)
#
# Exercise 2: Authentication CLI - Login:
# a={"malhar":"abc", "vinod":"charlie","twinkle":"rohan"}
# while True:
#     first = input("do you want to login, signup or quit? ")
#     if first=="quit":
#         break
#     elif first=="login":
#         second=input("share username and password? ")
#         second=second.split(",")
#         d=tuple(second)
#         user, pass=d()
#         print(second)
#         if ((user in a) and (a[user]==pass)):
#             print("login succesful")
#             logged_in=second[0]
#             break
#         else:
#             print("wrong username password")
#             break
  #  if first=="signup":
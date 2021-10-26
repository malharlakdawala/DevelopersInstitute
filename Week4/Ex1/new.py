# name = "toby"
# age = 4

# print(
#     f"helo {name} asdf {age} asdf")


# a = 5
# b = 6
# if a < b:
#     print(f"{b} is bigger")
# else:
#     print(f"{a} is bigger")

# #print("i love python\n"*5+"hellow rol \n"*5)

# a = int(input("enter month "))
# if 0 < a <= 3:
#     print("its spring")
# elif 3 < a <= 6:
#     print("its summer")
# elif 6 < a <= 9:
#     print("its summer")
# else:
#     print("its winter")

#mytext = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim"
# print(len(mytext))

a = input("input string kar bhai ")
if len(a) < 11:
    print("enter longer string")
else:
    print("too long")

print("end charctrs are ", a[0], a[len(a)-1])

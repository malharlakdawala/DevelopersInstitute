# a= "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
# print(len(a))

# 2
a = ""
b=""
a = input("enter word ")
if (len(a) > len(b)):
    print(f"longest word is {a}")
    b = a
else:
    print(f"longest word is {b}")

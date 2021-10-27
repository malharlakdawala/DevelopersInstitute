# Exercise 1: Formula
# c, h = (50, 30)
# d = input("Add comma separated numbers ")
# print(d)
# d = d.split(",")
# result1 = []
# for n in d:
#     n = int(n)
#     a=int((2*c*n/h)**0.5)
#     #a = c * h * n
#     # print(a)
#     result1.append(a)
# print(result1)
#
# Exercise 2 : List Of Integers
#
# a = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7, 22, 54]
# print(a)
# print(sorted(a, reverse=True))
# print(sum(a))
# print(a[0], a[-1])
# b = []
# for n in a:
#     b.append(n * n)
# print(b)
# print(sum(a) / len(a))
# print(f"remove duplicates: {list(set(a))}")
# print(max(a), min(a))
#
# Exercise 3: Working On A Paragraph
# a="Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)"
# print(len(a))
# b=a.count(".")
# print(f"no. of sentences are: {b}")
#
# Exercise 4
a= "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
a=a.split()
b=list(set(a))
for n in b:
    print(f"frequency of {n} is {a.count(n)}")
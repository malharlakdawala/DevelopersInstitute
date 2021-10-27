x=input("write sentence ")
x=x.split()
a=[]
for n in x:
   a.append(n[::-1])

print(" ".join(a))
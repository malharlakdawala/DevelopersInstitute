x=int(input("Enter number "))
b=x
a=[]
for n in range(1,x):
    if(x%(b-1)==0):
        a.append(b-1)
    b=b-1
if sum(a)==x:
    print(f"{x} is a perfect number")
else:
    print(f"{x} is NOT a perfect number")

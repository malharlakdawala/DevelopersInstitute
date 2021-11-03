import random

amount =10
count=0
while True:
    amount= amount+ random.choice([-1,1])
    count+=1
    if amount==0:
        print(count)
        break
        print(amount)
#Exc1
# for j in range(1,4):
#     print(" "*(3-j)+"*"*(2*j-1))

#Exc2
# for j in range(0,6):
#     print(" "*(6-j)+"*"*j)

#Exc3

# for i in range(0,6):
#     print("*"*i)
# for i in range(0,6):
#     print(" "*i+"*"*(6-i))

#Exc4

my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):
    minimum = i
    for j in range( i + 1, len(my_list)):
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)

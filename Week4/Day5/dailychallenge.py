#Approach1
# input_string = input("Enter Comma seperated string values ")
# input_data=input_string.split(",")
# print(sorted(input_data))
#
#Approach2
input_string = input("Enter Comma seperated string values ")
input_data=input_string.split(",")
sorted_data=input_data.copy()
temp=""
for j in range(len(input_data)):
    for i in range(len(input_data)-1):
        if input_data[i]>input_data[i+1]:
            temp=input_data[i]
            input_data[i]=input_data[i+1]
            input_data[i+1]=temp
print(input_data)
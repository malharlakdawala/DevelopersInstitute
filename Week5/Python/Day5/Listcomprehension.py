# nums = [i for i in range(1,1001)]
# print(nums)
# 1
# num=[i for i in range(1,1000) if i%8==0]
# 2
# num=[i for i in range(1,1000) if "6" in str(i)]
# 3
# string = "Practice Problems to Drill List Comprehension in Your Head."
# num=len([char for char in string if char==" "])
# 4
# vowels = ["a","e","i","o","u"]
# str = [char for char in string if char not in vowels]
# str="".join(str)
#
# 5

# str = string.split(" ")
# str1=[word for word in str if len(word)<5]
# print(" ".join(str1))
# print(num)

# 6
# str = string.split(" ")
# length = [len(word) for word in str]
# print(length)
#
# 7
# num = [i for i in range(1,100) if True in [True for j in range(2,9) if i%j==0]]
#
# print(num)
# 8
# list_a = [1, 2, 3, 4]
# list_b = [2, 3, 4, 5]
# num = [i for i in list_b if i in list_a]
# print(num)

# string = "In 1984 there were 13 instances of a protest with over 1000 people attending"
# str = string.split(" ")
# num = [word for word in str if not word.isalpha()]
# print(num)
#
# num=[i for i in range(1,20) is "even" if i%2==0]
# print(num)

# Dictionary Comprehension
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# sol = dict(zip(keys,values))
# print(sol)

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
#
# #dict1.update(dict2)
# dict3={**dict1,**dict2}
# print(dict3)

# sampleDict = {
#    "class":{
#       "student":{
#          "name":"Mike",
#          "marks":{
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])

# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
#
# emp_dict = dict.fromkeys(employees,defaults)
# print(emp_dict)

# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
#
# }
# # new_dict = {"name":sampleDict["name"],"age":sampleDict["age"]}
# # print(new_dict)
# keys = ["name", "salary"]
# new_dict= {key:sampleDict[key] for key in keys}
# print(new_dict)

# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
#
# }
# keysToRemove = ["name", "salary"]
#
# new_dict = {k:sampleDict[k] for k in sampleDict.keys()- keysToRemove}
# print(new_dict)
#
# sampleDict = {'a': 100, 'b': 200, 'c': 300}
# a= [i for i in sampleDict.values() if i==200]
# print(200 in sampleDict.values())
# print(a)
#
# sampleDict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# sampleDict["location"]=sampleDict.pop("city")
# print(sampleDict)

# sampleDict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
#
# # a=min([i for i in sampleDict.values()])
# a=min(sampleDict, key=sampleDict.get)
# print(a)

sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
sampleDict["emp3"]["salary"] = 8500
print(sampleDict)
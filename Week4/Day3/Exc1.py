# Exercise 1 : Convert Lists Into Dictionaries

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# a=dict(zip(keys,values))
# print(a)
#
# Exercise 2 : Cinemax #2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# price_of_ticket = 0
# sum=0
# for n in family:
#     if family[n] <= 3:
#         price_of_ticket = 0
#     elif 3 < family[n] <= 12:
#         price_of_ticket = 10
#     else:
#         price_of_ticket = 15
#     sum+=price_of_ticket
#     print(f"price for {n} is {price_of_ticket}")
# print(f"total sum is {sum}")
#
# names = input("Enter names of people? ")
# names=names.split()
# age = input("Enter age of those people")
# age=age.split()
# family=dict(zip(names,age))
# price_of_ticket = 0
# sum=0
# for n in family:
#     family[n]=int(family[n])
#     if family[n] <= 3:
#         price_of_ticket = 0
#     elif 3 < family[n] <= 12:
#         price_of_ticket = 10
#     else:
#         price_of_ticket = 15
#     sum+=price_of_ticket
#     print(f"price for {n} is {price_of_ticket}")
# print(f"total sum is {sum}")
#
# Exercise 3: Zara
#
# brand = {"name": "Zara",
#          "creation_date": 1975,
#          "creator_name": "Amancio Ortega Gaona",
#          "type_of_clothes": ["men", "women", "children", "home"],
#          "international_competitors": ["Gap", "H&M", "Benetton"],
#          "number_stores": 7000,
#          "major_color": {
#              "France": "blue",
#              "Spain": "red",
#              "US": ["pink", "green"]}}
# brand["number_stores"] = 2
# print(
#     f'Competitors of {brand["name"]} are {brand["international_competitors"][0]}, {brand["international_competitors"][1]}, and {brand["international_competitors"][2]}')
# brand["country_creation "] = "Spain"
# if "international_competitors" in brand.keys():
#     brand["international_competitors"].append("Desigual")
# del brand["creation_date"]
# print(brand["international_competitors"][-1])
# for n in brand["major_color"]:
#     print(f'major colours are {brand["major_color"][n]}')
# print(brand["major_color"].values())
# # print(len(brand))
# # print(brand.keys(),brand.values())
# # print(brand)
# more_on_zara = {"creation_date": 1975,
#                 "number_stores": 10000
#                 }
# brand.update(more_on_zara)
# print(brand["number_stores"])
#
# Exercise 4 : Disney Characters

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
new_users=sorted(users)
new_dict_1={}
new_dict_2={}
new_dict_3={}
count=0
for n in users:
    new_dict_1[n]=count
    new_dict_2[count]=n
    count+=1
print(new_dict_1)
print(new_dict_2)
count=0
for n in new_users:
    new_dict_3[n]=count
    count+=1
print(new_dict_3)
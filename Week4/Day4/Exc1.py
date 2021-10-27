# Exercise 1 : What Are You Learning ?

# def display_message():
#     print("learning python ")
# display_message()
#
# Exercise 2: What’s Your Favorite Book ?
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")
# favorite_book("Alice in Wonderland")
#
# Exercise 3 : Some Geography
# def describe_city(name_of_city, country):
#     print(f"{name_of_city} is in {country}")
# describe_city("Mumbai","India")
#
# Exercise 4 : Random
# import random
# def rand_func(num):
#     a=random.randint(1,100)
#     if num==a:
#         print("numbers are equal")
#     else:
#         print("numbers are not equal")
# rand_func(10)
#
# Exercise 5 : Let’s Create Some Personalized Shirts !
# def make_shirt(size="Large",text="I love Python"):
#     print(f"tshirt size is {size} and text to print is {text}")
# make_shirt()
# make_shirt("Small",)
# make_shirt("Medium","Random Message")
# make_shirt(text="Random text",size="Small")
#
# Exercise 6 : Magicians
magician_name = ["Blaine", "Apllo", "Mindreader", "Abra ka Dabra"]
def show_magicians(name_lsit):
    print(name_lsit)
def make_great(name_list):
    for n in range(0,len(name_list)-1):
        name_list[n] = "The Great "+name_list[n]

make_great(magician_name)
show_magicians(magician_name)


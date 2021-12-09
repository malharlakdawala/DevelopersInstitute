# def my_decorator(my_function):    # <-- (4)
#     def inner_decorator():        # <-- (5)
#         print("This happened before!")  # <-- (6)
#         my_function()             # <-- (7)
#         print("This happens after ")    # <-- (10)
#         print("This happened at the end!")    # <-- (11)
#     return inner_decorator
#     # return None
#
#
# @my_decorator       # <-- (3)
# def my_decorated():    # <-- (2) <-- (8)
#     print("This happened!")   # <-- (9)
#
#
# my_decorated()    # <-- (1)

#
# def cap_decorator(func):
#     def wrapper(name):
#         name = name.capitalize()
#         func(name)
#     return wrapper
#
# @cap_decorator
# def print_my_name(name):
#     print("Hello world from",name)
#
# @cap_decorator
# def say_hello_to_me(name):
#     print("Hello to",name)
#
# print_my_name("eyal")
# say_hello_to_me("eyal")

# def cap_decorator(func):
#     def wrapper(*args, **kwargs):
#         args = [arg.capitalize() for arg in args]
#         func(*args, **kwargs)
#     return wrapper
#
# @cap_decorator
# def describe_me(first_name, last_name, favourite_activity):
#     print("I am {} {} and I love {}".format(first_name, last_name, favourite_activity))
#
# @cap_decorator
# def describe_my_family(father_name, mother_name, brother_name, sister_name):
#     print("The name of my father is", father_name)
#     print("The name of my mother is", mother_name)
#     print("The name of my brother is", brother_name)
#     print("The name of my sister is", sister_name)
#
# describe_me("john", "ricotta", "coding")
# describe_my_family("John","Valentina","mario","luigi")

# import datetime
#
#
# def my_decorator(inner):
#     def inner_decorator(num_copy):
#         print(datetime.datetime.utcnow())
#         inner(int(num_copy) + 1)
#         print(datetime.datetime.utcnow())
#     return inner_decorator
#
#
# @my_decorator
# def decorated(number):
#     print("This happened : " + str(number))
#
# decorated(5)

# def decorator_creator(city):
#     def decorator(func):
#         def new_function(*args, **kwargs):
#             print("Hello world from", city)
#             func(*args, **kwargs)
#         return new_function
#     return decorator
#
# @decorator_creator("Tel Aviv")
# def my_function():
#     print("Hello from my function")
#
# my_function()

def first_decorator(f):
    def wrapper():
        print("Hello from decorator 1")
        f()
    return wrapper

def second_decorator(f):
    def wrapper():
        print("Hello from decorator 2")
        f()
    return wrapper

@first_decorator
@second_decorator
def simple_function():
    print("Hello world!")

simple_function()

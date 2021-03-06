#Exercise 1
# default_list = [454,"asdf",[3,5,"erwe"],"afsd",34]
# default_list.insert(2,[3,"asdf"])
#
# print(default_list)
#
# Exercise 2
# input_string = "my name is malhar"
# print(f'the no. of spaces are {input_string.count(" ")}')
#
# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.
# input_string = "My Name is Malhar"
# count_upper= sum(True for i in input_string if i.isupper())
# count_lower= sum(True for i in input_string if i.islower())
#
# print(count_upper,count_lower)

#
# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:
#
#     >>>my_sum([1,5,4,2])
#     >>>12

# def my_sum(*args):
#     sum=0
#     for i in args[0]:sum+=i
#     return sum
# print(my_sum([1,5,4,2]))


# Exercise 5
# Instructions
# Write a function to find the max number in a list
#
#     >>>find_max([0,1,3,50])
#     >>>50
# def find_max(*args):
#     max_value=0
#     temp=0
#     for i in args[0]:
#         if i>max_value: max_value=i
#     return max_value
# print(find_max([0,1,3,50]))
# Exercise 6
# Instructions
# Write a function that returns factorial of a number
#
#     >>>factorial(4)
#     >>>24

# def factorial(num):
#     prod=1
#     while num!=0:
#         prod=prod*num
#         num-=1
#     return prod
# print(factorial(4))
#
# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):
#
#     >>>list_count(['a','a','t','o'],'a')
#     >>>2
# def list_count(*args):
#     count=0
#     for i in args: count+=1
#     return count
# print(list_count(['a','a','t','o'],'a',5))
# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
#
#     >>>norm([1,2,2])
#     >>>3


# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)
#
#     >>>is_mono([7,6,5,5,2,0])
#     >>>True
#
#     >>>is_mono([2,3,3,3])
#     >>>True
#
#     >>>is_mono([1,2,0,4])
#     >>>False
#
#
# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.
#
#
# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
#
#
# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:
#
#     >>>is_palindrome('radar')
#     >>>True
#
#     >>>is_palindrome('John)
#     >>>False
#
#
# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:
#
#     >>>sentence = 'Do or do not there is no try'
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3
#
#
# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):
#
#     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#     >>>3
#
#
# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:
#
#     >>>common_div(10,20)
#     >>>[2,5,10]
#
#
# Exercise 16
# Instructions
# Write a function that test if a number is prime:
#
#     >>>is_prime(11)
#     >>>True
#
#
# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:
#
#     >>>weird_print([1,2,2,3,4,5])
#     >>>[2,4]
#
#
# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:
#
#     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2
#
#
# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.
#
#
# Exercise 20
# Instructions
# Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"
#
#

# def box_printer(*args):
#     length_of_largest_word=0
#     for arg in args:
#         if (length_of_largest_word<len(arg)): #could have used len(max(args))
#             length_of_largest_word=len(arg)
#     print(length_of_largest_word)
#     print("*"*(4+length_of_largest_word))
#     for arg in args:
#         print("* "+arg+" "*(length_of_largest_word-len(arg))+" *")
#     print("*"*(4+length_of_largest_word))
#
# box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
#
#
# Exercise 2
def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)

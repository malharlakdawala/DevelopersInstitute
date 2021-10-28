#Exercise 7: When Will I Retire ?

# def get_age(year, month, day):
#     return 2021-int(year)
#
# def can_retire(gender, date_of_birth):
#     age_person=get_age(date_of_birth[-4:],date_of_birth[3:5],date_of_birth[0:2])
#     if(gender=="f" and age_person>=62):print("you can retire")
#     elif(gender=="f" and age_person<62):print("you can not retire")
#     elif(gender=="m" and age_person<67):print("you can not retire")
#     elif(gender=="m" and age_person>=67):print("you can retire")
#
# can_retire("f","02/05/1958")
#
# Exercise 8:

def add_four(x):
    sum=0
    a=x
    for n in range(0,4):
        sum=sum+int(a)
        a=a+x
        print(a)
    print(sum)
add_four("3")


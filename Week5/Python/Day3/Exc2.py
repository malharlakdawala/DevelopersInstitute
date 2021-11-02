# # Exercise 1
import datetime

#
# today_date = datetime.datetime.now()
# print(today_date)
# #Exc2
#
# Jan1st_date = datetime.datetime(2022,1,1)
#
# timediff = Jan1st_date-today_date
#
# print(f"the 1st of January 2022 is in {timediff} hours")

# Exc3

# def birthdate(dd,mm,yyyy):
#     bdate = datetime.datetime(yyyy,mm,dd)
#     tdate = datetime.datetime.now()
#     tdiff = tdate-bdate
#     print(f"you are alive for {tdiff.total_seconds()/60} minutes")
#
# birthdate(20,11,1989)
#  Exc5

# planets = {"earth": 365.25, "mercury": 0.24, "venus": 0.615, "mars": 1.88}
# def how_old(secs):
#     for k,y in planets.items():
#         if k == "earth":
#             print(f"you will be {secs / (31557600)} years old on {k} planet")
#         else:
#             print(f"you will be {secs/(y*31557600)} years old on {k} planet")
# how_old(1000000000)
#
# Exercise 6 : Faker Module
from faker import Faker
users=[]
fake_name = Faker()
for i in range(10):
    users.append({
            "name":fake_name.name(),
           "address":fake_name.address(),
    })
# for i in range(10):
#     print(users[i]["name"],users[i]["address"])

print([users[i]["name"] for i in range(0,10)])
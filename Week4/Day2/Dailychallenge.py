
age = input("Enter birthdate in dd/mm/yyyy format? ")
age_year = age[-4:]
age_in_2021 = 2021-int(age_year)
last_character=age_in_2021 % 10
c=" "*7+"_"*(5-int(last_character/2))+"i"*last_character+"_"*(5-int(last_character/2))+" "*7

print(c)


a="""      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""
print(a)
'''

       ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

'''
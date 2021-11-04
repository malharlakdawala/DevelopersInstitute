# Exercise 1 – Random Sentence Generator
#
# import random
# def get_words_from_file():
#     with open("words.txt", 'r') as file:
#         text = file.read()
#         print(text)
#
# a = []
# def get_random_sentence(length):
#     with open("words.txt", 'r') as file:
#         text = file.readlines()
#         for i in range(length):
#             b = text[random.randint(1, 20)]
#             b = b.split("\n")
#             a.append(b[0].lower())
#     print(*a)
#
# userinput = int(input("please enter a number between 2 and 20: "))
# if 2<userinput<20:
#     get_random_sentence(userinput)
# else:
#     raise TypeError("number should be between 2 and 20")
#
# Exercise 2: Working With JSON
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


json_object =json.loads(sampleJson)
#print(json_object)
print(json_object["company"]["employee"]["payable"]["salary"]) #salary
json_object["company"]["employee"]["birth_date"]="20/11/1989"
print(json_object)
with open("samplefile.json","w") as file:
    json.dump(json_object,file)
import json
with open("file.json","r") as file:
    txt = json.load(file)
print(txt)
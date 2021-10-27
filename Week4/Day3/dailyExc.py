input_text = input("input text ")
check =input("encode or decode ")
cypher_text=""
if check=="encode":
    for letter in input_text:
        cypher_text += chr(ord(letter) + 3)
else:
    for letter in input_text:
        cypher_text += chr(ord(letter) - 3)
print(cypher_text)
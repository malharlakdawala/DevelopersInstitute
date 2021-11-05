class Anagramchecker:
    def __init__(self, user_word):
        self.user_word = user_word
        with open("words.txt", "r") as file:
            text = file.read()
        self.text = text.split("\n")
        if user_word in self.text:
            print("valid word")
        else:
            print("invalid word")

    def get_anagrams(self):
        a = []
        word_modify = sorted([char for char in self.user_word])
        for i in self.text:
            b = sorted([char for char in i])
            if (len(word_modify) == len(b) and len(word_modify) == sum([1 for k, j in zip(word_modify, b) if k == j])):
                a.append(i.lower())
        return a


#Anagramchecker("MEAT").get_anagrams()

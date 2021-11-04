from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize

class Text:
    def __init__(self, str):
        self.str = str
        self.a = self.str.split(" ")

    def no_of_words(self):
        count = len(self.a)
        print(count)

    def common_word(self):
        self.b = {}
        for i in range(len(self.a)):
            if self.a[i] not in self.b:
                self.b[self.a[i]] = 1
            else:
                self.b[self.a[i]] = self.b[self.a[i]] + 1
        print(self.b)

    def unique_words(self):
        print(self.b.keys())

    def from_file(self, filename):
        with open(filename, "r") as file:
            return file.read()


class TextModification(Text):
    def __init__(self, str):
        super().__init__(str)
        pass

    def without_punctuation(self):
        a=self.str
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for ele in a:
            if ele in punc:
                a=a.replace(ele,"")
        print(a)

    def stop_words(self):
        # b=self.str.split(" ")
        # stop_words=["a","and","the"]
        # c=len(b)
        # for i in range(c):
        #     for ele in stop_words:
        #         if b[i] == ele:
        #             del b[i]
        #             c-=1
        #             print(c)
        #     if i==c-2:
        #         break
        #
        # print(*b)
        b=word_tokenize(self.str)
        string_without_sw=[word for word in b if not word in stopwords.words()]
        print(*string_without_sw)





str1 = Text(
    "What are you trying to achieve? python2 and trying python3 both throw 'TypeError', which means the caller trying is misusing the function 'fun'")

# str1.no_of_words()
# str1.common_word()
# str1.unique_words()
# c = Text.from_file("","words.txt")
# print(c)
str2 = TextModification(
    "Create a class called Text that takes a ;,. string as an argument and store the text in a attribute a")
str2.without_punctuation()
str2.stop_words()

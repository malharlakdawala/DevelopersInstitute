import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']
word = random.choice(wordslist)
word_masked = "*" * len(word)
word=word.split()
print(word)
word_masked_list=word_masked.split()
print(f'lets start, the word is {word_masked}')
while True:
    input_character = input("Enter single character ")
    for n in range(len(word)):
        if input_character in word:
            word_masked_list[n]=input_character
    print(word_masked_list)

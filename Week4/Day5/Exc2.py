import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']
word = random.choice(wordslist)
word_masked = "*" * len(word)
word=list(word)
print(word)
word_masked_list=list(word_masked)
print(f'lets start, the word is {word_masked}')
count=6
while True:
    if(count==0):
        print("Game Over")
        break
    else:
        input_character = input(f"Enter single character, total chances left are {count} ")
        for n in range(len(word)):
            if input_character == word[n]:
                word_masked_list[n]=input_character
        print(*word_masked_list)
        count-=1
        if word_masked_list==word:
            print("You Win")
            break

#covert word to list, using list(), make a copy of the generated word's length,
#for each new letter, check if it is there in original word, if yes, convert index of that word in masked list to input letter
#loop this through lenght of word, to check for multiple occurances
#loop entire code for 6 counts
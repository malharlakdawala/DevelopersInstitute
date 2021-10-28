def count_characters(string, character):
    count=0
    for i in range(len(string)):
        if character == string[i]: count+=1
    print(count)

count_characters("I love asfdasaaadfafd India","a")
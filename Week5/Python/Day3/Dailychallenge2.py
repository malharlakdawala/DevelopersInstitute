a = []
class Dailychallenge:
    def __init__(self, name, age, score):
        global a
        self.name = name
        self.age = age
        self.score = score
        self.store=(self.name,self.age,self.score)
        a.append(self.store)
       # print(a)


    def sorting(self):
        for i in range(len(a)-1):
            j=0
            for k in range(len(a[i])):
                if a[i][j]==a[i+1][j]:
                    if a[i][j+1]==a[i+1][j+1]:
                        if a[i][j+2]>a[i+1][j+2]:
                            temp=a[i]
                            a[i]=a[i+1]
                            a[i+1]=temp
                    elif a[i][j+1]>a[i+1][j+1]:
                        temp = a[i]
                        a[i] = a[i + 1]
                        a[i + 1] = temp
                elif a[i][j]>a[i+1][j]:
                    temp = a[i]
                    a[i] = a[i + 1]
                    a[i + 1] = temp
        print("the sorted list is: ", a)


#a=[('Tom', 19, 80), ('John', 20, 90), ('Jony', 17, 91), ('Jony', 17, 93)]


user1 = Dailychallenge("Tom", 19, 80)
user2 = Dailychallenge("John", 20, 90)
user3 = Dailychallenge("Jony", 17, 91)
user4 = Dailychallenge("Jony", 17, 93)
user5 = Dailychallenge("Json", 21, 85)
user5.sorting()

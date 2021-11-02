import random

class Organism:
    def __init__(self, environment, dna_obj):
        self.environment = environment
        self.dna_obj = dna_obj
        self.li = []

    def mutate(self):
        counter = 0
        while True:
            counter += 1
            gene = [0, 1, self.environment]
            self.dna_obj[random.choice(range(10))] = random.choice(gene)
            if self.dna_obj.count(1) == 10:
                print(self.dna_obj)
                self.li.append(counter)
                print(counter)
                break


a = Organism(1, [1, 1, 0, 1, 1, 1, 0, 1, 1, 0])
c = Organism(1, [1, 1, 1, 1, 0, 1, 0, 1, 1, 0])
b = Organism(5, [1, 1, 1, 1, 1, 0, 0, 1, 1, 0])

a.mutate()
b.mutate()
c.mutate()

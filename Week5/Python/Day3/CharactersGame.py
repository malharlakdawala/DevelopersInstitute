class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, other):
        pass


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life=20, attack=10)
        print(f"{self.name} the Druid is created")

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, other):
        other.life = other.life - (0.75 * self.life + 0.75 * self.attack)

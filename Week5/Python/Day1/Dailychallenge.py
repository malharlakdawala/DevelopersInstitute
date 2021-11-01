class Farm:
    def __init__(self, name):
        self.name = name
        self.store_list = {}

    def add_animal(self, animal_name, qty=1):
        if animal_name in self.store_list:
            self.store_list[animal_name] += qty
        else:
            self.store_list[animal_name] = qty

    def get_info(self):
        str = ""
        for k in self.store_list:
            str = str + f"{k}:{self.store_list[k]} \n"

        str = str + "E-I-E-I-0!"
        return str
    def get_animal_types(self):
        return self.get_info()

    def get_short_info(self):
        str=""
        for k in self.store_list:
            str = str + ", " + k
        return f"McDonald’s farm has {str}"



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())

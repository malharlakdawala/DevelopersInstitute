class Farm:
    def __init__(self,name):
        self.name=name

    def add_animal(self,animal_name,qty=1):
        if qty<2:
            if animal_name in 


    def get_info(self):
        return "E-I-E-I-0!"

macdonald = Farm("McDonald")
macdonald.add_animal('sheep')
macdonald.add_animal('sheep',5)
print(macdonald.get_info())

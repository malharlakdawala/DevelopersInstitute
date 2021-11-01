class Farm:
    def __init__(self,name):
        self.name=name
        self.store_list={}

    def add_animal(self,animal_name,qty=1):
        if animal_name in self.store_list:
            self.store_list[animal_name]+=qty
        else:
            self.store_list[animal_name]=qty


    #checks keys


    #    if key in [sub for ele in ]
        # for i in self.store_list:
          #     if animal_name == i[0]:
        #         print("hi")
        #     else: print("no hi")

            # if self.store_list
            #     print("hi")
            # # if list.__contains__(animal_name):
            # #     print("hi")
            # #     self.store_list[i].qty = self.store_list[i].qty + qty
            # else:
            #     print("hello")
            #     self.store_list.append({animal_name: qty})
            # print(self.store_list)


    def get_info(self):
        return "E-I-E-I-0!"

macdonald = Farm("McDonald")
macdonald.add_animal('sheep')
macdonald.add_animal('sheep',5)
print(macdonald.get_info())

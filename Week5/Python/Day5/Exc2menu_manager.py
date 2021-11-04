import json

class MenuManager:
    def __init__(self):
        with open("menu.json", "r") as file:
            self.menu = file.read()
            self.menu = json.loads(self.menu)

    def add_item(self, name, price):
        self.menu["items"].append({"name": name, "price": price})
        print("item added ",self.menu["items"])

    def remove_item(self,name):
        self.menu["items"]= [item for item in self.menu["items"] if name not in item["name"]]
        print("item removed",self.menu["items"])

    def save_to_file(self):
        self.menu=json.dumps(self.menu,indent=2)
        with open("menu.json", "w") as file:
            file.write(self.menu)

    def show_menu(self):
        for i in range(len(self.menu["items"])):
            print(self.menu["items"][i]["name"], self.menu["items"][i]["price"])


# menu1 = MenuManager()
# menu1.add_item("idli", 45)
# menu1.remove_item("Hamburger")
# menu1.save_to_file()
# menu1.show_restaurant_menu()

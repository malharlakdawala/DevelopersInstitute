import psycopg2
import psycopg2.extras

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'varlamov'
DATABASE = 'menu'


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def run_query(self, query):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()

    def save(self):
        query = f"insert into menu (item_name, price) values ('{self.name}', '{self.price}')"
        self.run_query(query)

    def delete(self):
        query = f"delete from menu where item_name = '{self.name}' and price = {self.price}"
        self.run_query(query)

    def update(self, name, price):
        query = f"update menu set item_name = '{name}', price = {price} where id = 1"
        self.run_query(query)

    def delete_rows(self):
        query = f"TRUNCATE TABLE menu RESTART IDENTITY"
        self.run_query(query)

    def all():
        query = "select * FROM menu"
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        return results

    def get_by_name(name):
        query = f"SELECT * FROM menu where item_name = '{name}'"
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        connection.close()
        for item in results:
            print(item)


item = MenuItem('Burger', 35)
item3 = MenuItem('Beef Stew', 36)
item.delete()
item.delete_rows()
item.save()
item3.save()
item.update('Veggie Burger', 37)
items = MenuItem.all()
print(items)
item2 = MenuItem.get_by_name('Beef Stew')
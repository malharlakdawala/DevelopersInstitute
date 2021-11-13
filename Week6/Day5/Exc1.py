import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'root'
DATABASE = 'MenuPython1'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()

class MenuItem:
    def __init__(self):
        pass

    def save(self, name1, price1):
        query = f"INSERT INTO menuitem (name,price) values ('{name1}',{price1});"
        cursor.execute(query)
        connection.commit()
        print("item added succesfully ")

    def delete(self, name):
        query = f"delete from menuitem where name='{name}';"
        cursor.execute(query)
        connection.commit()
        print("item deleted succesfully ")

    def update(self, name, price):
        query = f"update menuitem set price={price} where name='{name}';"
        cursor.execute(query)
        connection.commit()
        print("item updated succesfully ")

    def all(self):
        print("full data is: ")
        query = f"select*from menuitem"
        cursor.execute(query)
        connection.commit()
        result= cursor.fetchall()
        for i in result:
            print(i)

    def get_by_name(self, name):
        query = f"select*from menuitem where name='{name}';"
        cursor.execute(query)
        connection.commit()
        result = self.run_query(query)
        for i in result:
            print(i)

# item = MenuItem()
# # item.save('Veggie Burger', 36)
# # item.save('Dosa', 46)
# # item.save('Idli', 32)
# item.update('Idli', 58)
# item.all()
# connection.close()
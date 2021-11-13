import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'root'
DATABASE = 'MenuPython1'


class MenuItem:
    def __init__(self):
        pass

    def save(self, name1, price1):
        query = f"INSERT INTO menuitem (name,price) values ('{name1}',{price1});"
        return self.run_query(query)

    def delete(self, name):
        query = f"delete from menuitem where name='{name}';"
        return self.run_query(query)

    def update(self, name, price):
        query = f"update menuitem set price={price} where name='{name}';"
        return self.run_query(query)

    def all(self):
        query = f"select*from menuitem"
        result= self.run_query(query)
        for i in result:
            print(i)

    def get_by_name(self, name):
        query = f"select*from menuitem where name='{name}';"

    def run_query(self, query):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        # if cursor.fetchall():
        #     results = cursor.fetchall()
        # else: results = ''
        connection.close()
        # return results


item = MenuItem()
item.save('Burger', 55)
#item.all()
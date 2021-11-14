import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'root'
DATABASE = 'MenuPython1'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()


def userinput():
    userinput = input("""
    What do you want to do?
    l-> Login
    s-> Signup
    x-> Exit    
    """)
    if userinput == "l":
        user_pass_chk()
    elif userinput == "s":
        signup()
    elif userinput == "x":
        connection.close()
        exit()
    else:
        print("Wrong input, please try again")
        userinput()


def user_pass_chk():
    username = input("Please share username: ")
    password = input("Please share password: ")
    query = f"SELECT EXISTS(SELECT * FROM loginsignup WHERE username='{username}')"
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchone()
    if result[0] == True:
        query = f"select password from loginsignup where username='{username}'"
        cursor.execute(query)
        connection.commit()
        result = cursor.fetchone()
        if result[0] == password:
            print("Login Succesfull")
            userinput()
        else:
            print("Wrong username password,please try again ")
            user_pass_chk()
    else:
        print("Wrong username password,please try again ")
        user_pass_chk()

def signup():
    username = input("Please share username: ")
    password = input("Please share password: ")
    query = f"SELECT EXISTS(SELECT * FROM loginsignup WHERE username='{username}')"
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchone()
    if result[0]:
        print("username already present, please try again. ")
        signup()
    else:
        query = f"insert into loginsignup (username,password) values ('{username}','{password}')"
        cursor.execute(query)
        connection.commit()
        print(f"Signup successful for username: {username}")
        userinput()


userinput()

import json
import random

import psycopg2
import requests

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'root'
DATABASE = 'MenuPython1'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)

api_key = "6093e2f571371906610bafc6d866a247"
api_url = "http://api.countrylayer.com/v2/all"
paramters = {"access_key": api_key}
response = requests.get(api_url, params=paramters)

if response.status_code == 200:
    response = response.json()

# print(response)

for n in range(10):
    i=random.randint(0,100)
    name = response[i]["name"]
    capital = response[i]["capital"]
    topleveldomain = response[i]["topLevelDomain"][0]
    region = response[i]["region"]

    query = f"INSERT INTO countries (name,capital,topleveldomain,region) values ('{name}','{capital}','{topleveldomain}','{region}');"
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

connection.close()

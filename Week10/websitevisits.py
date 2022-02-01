import random
import time

import requests

URL = "https://www.educative.io/edpresso/how-to-do-arithmetic-operations-in-postgresql"
for i in range(1,500):
    r = requests.post(url = URL)
    print("hit number: ",i, r)
    time.sleep(random.randint(5,15))

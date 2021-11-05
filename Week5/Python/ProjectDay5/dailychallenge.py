import time
from datetime import datetime
import requests

time_start = datetime.now()
req=requests.get("https://www.facebook.com/")
print(req)
time_stop = datetime.now()
print(time_stop - time_start)

import requests

URL = "http://2factor.in/API/V1/293832-67745-11e5-88de-5600000c6b13/ADDON_SERVICES/SEND/TSMS"
data = {'From': "TFCTOR", 'To': "9769494336", 'Msg': "Hello World"}
r = requests.post(url = URL, data = data)
print(r.text)

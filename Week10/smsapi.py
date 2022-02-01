import requests

URL = "http://2factor.in/API/V1/3adf9525-efb4-11eb-8089-0200cd936042/ADDON_SERVICES/SEND/TSMS"
data = {'From': "ERSSTD", 'To': "9769494336","TemplateName":"OTPVerification3" , "Var1":"ee"}
r = requests.post(url = URL, data = data)
print(r.json)

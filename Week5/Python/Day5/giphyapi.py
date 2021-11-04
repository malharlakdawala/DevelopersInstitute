# readable
# commenting your code
# technical complexity - heavyload
# recursive function -> avoid
import json
import requests

input_keyword = "laugh"
api_url = "https://api.giphy.com/v1/gifs/search"
api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
parameters = {"api_key": "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My", "q": "laugh"}
response = requests.get(api_url, params=parameters)

# api_request_url = f"{api_url}?&q={input_keyword}&api_key={api_key}&limit=5"
# print(api_request_url)
# response = requests.get(api_request_url, params)
if response.status_code == 200:
    response = response.json()
    # response = json.load(response)
    #    print(response)
print(response['data'][0]['images']['original']['height'])

# unable to fetch values from json response

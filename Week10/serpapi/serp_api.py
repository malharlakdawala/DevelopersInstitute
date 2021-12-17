from serpapi import GoogleSearch

secret_api = '309b109ea8fc68c4b3b2ce8b89d85bb9f9cf975f59359'

# params = {
#     "q": "kirana store pali rajasthan",
#     "location": "rajasthan, india",
#     "tbm": "lcl",
#     "api_key": "309b109ea8fc68c4b3b2ce8b89d85bb9f9cf975f59359bf"
# }

params = {
  "engine": "google_maps",
  "q": "kirana store",
  "ll": "@25.771315,73.323685,15.1z",
  "type": "search",
  "api_key": "309b109ea8fc68c4b3b2ce8b89d85bb9f9cf975f59359bf6c09"
}


search = GoogleSearch(params)
results = search.get_dict()
# local_results = results['local_results']
print(results)

import requests
import json

# url = "https://product.hr.frejun.com/api/v1/integrations/create-call/"
#
# parameters = {
#     "recruiter_email": "zeel.mehta@kapso.in",
#     "transaction_id": "1",
#     "job_id": "SDE",
#     "candidate_id": "1",
#     "candidate_number": "9109619057829",
#     "candidate_name": "Jargon"
# }
#
# r = requests.post(url, headers={'Authorization': 'Api-Key zRyfu7IZ.Ni1nkhbLhj2TfYgF0c'},data=parameters)
#
# print(r.text)


url1 = "https://product.hr.frejun.com/api/v1/integrations/calls/?page_size=8"
page_size = 8
params = {page_size: page_size}
r1 = requests.get(url1, headers={'Authorization': 'Api-Key zRyfu7IZ.Ni1nkhbLhj2TfYg'}, params=params)
print(r1.text)

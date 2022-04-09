'''This file Tests the deployed application by sending post request as json data format'''

import requests

headers = {'Content-type': 'application/json'}
prediction = requests.post('https://dpschallenge2022.ew.r.appspot.com/prediction', headers=headers, json= {'year': 2021, 'month': 2})

print(prediction.json())

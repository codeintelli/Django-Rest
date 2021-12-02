import requests
import json
URL = "http://127.0.0.1:8000/stu/create/"

data = {
    'name':'Mahadev',
    'roll':22222,
    'city':'Kailashc'
}

json_data = json.dumps(data)
print(json_data)

r = requests.post(url = URL,data = json_data)

data = r.json()
print(data)
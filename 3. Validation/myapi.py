import requests
import json

URL = "http://127.0.0.1:8000/stu/";

# ~ get data
# ~ get specific data
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    if id is not None:
        return print("id  = ", id ,"=" , data)
    
    print(data)

# ~ insert data

def post_data():
    data = {
        'name':'bholenath',
        'roll': 13121,
        'city': 'somnath'
    }
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data)
    data = r.json()
    print(data)
    print(' \n *********************after insert data********************* \n')
    get_data()


# ~ update data
def update_data():
    # for partial means only some data you want to updated
    # data = {
    #     'id':'8',
    #     'name':'sankar',
    #     'city': 'mahakal'
    # }
    # for full means you can update whole table row in this you need all columns details
    data = {
        'id':'8',
        'name':'dushyant',
        'city': 'sankar',
        'roll': 1323232
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)
    print(' \n *********************after insert data********************* \n')
    get_data()



# ~ delete data 
def delete_data():
    data = {'id':9}
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
    print(' \n *********************after insert data********************* \n')
    get_data()
    

# ~ get data
print('\n *********************before insert data********************* \n')
get_data()
# ~ get specific data
# get_data(1)
# ~ insert data
# print('\n')
# post_data()
# print('\n')
# ~ update data
# print('\n')
# update_data()
# print('\n')
# ~ delete data 
print('\n')
delete_data()
print('\n')
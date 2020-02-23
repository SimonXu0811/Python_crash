# Json is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"firstname":"Jhon", "lastname":"Doe", "age": 37}'

# Prase to an dic
user = json.loads(userJSON)
print(type(user))
print(user['firstname'])

cars = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON = json.dumps(cars)
print(carJSON)
print(type(carJSON))
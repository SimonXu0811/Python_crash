# Dictionaries is a collection which is unordered, changebale, indexed. No duplicate memebers

# Create dict
person = {
    'first_name': 'Jhon',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')
# print(person2, type(person2))

# Get Value
# print(person['first_name'])
# print(person.get('last_name')) 

# Add key/value
person['phone'] = '555-555-5555'
# print(person)

# Get dict keys
# print(person.keys())

# Get dict items
# print(person.items())

# Copy a dict
person2 = person.copy()
person2['city'] = 'Boston'
# print(person2)

# Remove a item
del(person['age'])
person.pop('phone')

# Clear a dict
# person.clear()

# Get length
print(len(person2))

# A list of dict
people = [
    {'name': 'Mary', 'age': 20},
    {'name': 'Bob', 'age': 30}
]

print(people[1]['name'])
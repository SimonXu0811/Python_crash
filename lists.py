# A List is a collection which is ordered and changeable. Allows duplicate members

# Lists are zero based

# Create List
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1,2,3,4,5))

# print(numbers, numbers2)

# Get a single value from a list
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Apples')

# Insert into position
fruits.insert(0, 'Apples')

# Change value
fruits[0] = 'Strawberry'

# Remove from certain position
fruits.pop(2)

# Reserve list
fruits.reverse()

# Sort list
fruits.sort()

# Reserve Sort list
fruits.sort(reverse = True)

print(fruits)

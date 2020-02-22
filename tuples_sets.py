# Tuple is a collection which is sorted and unchangeable. Allows duplicate members

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# If tuple just contain one member, should use trailing comma
fruits2 = ('Apples', )
# print(fruits2, type(fruits2))

# To get a value from tuple
# print(fruits[1])

# Cannot change value in tuple
# fruits[0] = 'Strawberry' X
# print(fruits)

# delete a tuple
del fruits2

# find the length of tuple
print(len(fruits))




# Set is a collection which is unordered and unindexed. Don't allow duplicated memebers

# Create a set
fruits_set = {'Apples', 'Oranges', 'Grapes'}

# Check if in a set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Mangos')

# Add duplicate
fruits_set.add('Apples')

# Remove from set
fruits_set.remove('Grapes')

# Clear set
fruits_set.clear()

# delete a set
del fruits_set
print(fruits_set)

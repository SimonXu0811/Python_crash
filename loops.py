# A loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set or a string)

people = ['Jhon', 'Paul', 'Sara', 'Susan']

# Simple for loop
# for person in people:
#     print(f'current person is {person}')

# Break
# for person in people:
#      if person == 'Sara':
#         break
#      print(f'current person is {person}')

# Continue
# for person in people:
#     if person == 'Sara':
#         continue
#     print(f'current person is {person}')

# range
# for i in range(len(people)):
#     print(f'current person is {people[i]}')

# range(x, y) start with x and end with y - 1
# for i in range(0,11):
#     print(f'Number is : {i}')


# While loops execute a set of statements as long as condition is true

count = 0
while count < 10:
    print(f'Number is {count}')
    count += 1
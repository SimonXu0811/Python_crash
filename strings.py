# Strings in python are surronded by either single or double qoutation marks.

name = 'Simon'
age = 21

# Concatenate insert a variable into string
# print('My name is ' + name + 'And I am ' + str(age))

# String Formating

# Arguments by position 
# print('My name is {name} and I am {age}'.format(name = name, age = age))

#F-Strings (3.6+)
# print(f'Hello, my name is {name}, and I am {age}')

# String methods
s = 'hello World'

# Capitalize Strings
print(s.capitalize())

# Make all Upper Case
print(s.upper())

# Make all Lower Case
print(s.lower())

# Swap Case
print(s.swapcase())
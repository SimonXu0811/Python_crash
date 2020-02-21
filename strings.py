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
# print(s.capitalize())

# Make all Upper Case
# print(s.upper())

# Make all Lower Case
# print(s.lower())

# Swap Case
# print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('World', 'everyone'))

# Count
substr = 'h'
print(s.count(substr))

# Start with return true of false
print(s.startswith('hello'))

# End with return true of false
print(s.endswith('d'))

# Spit into a list
print(s.split())

# Find position return the find position
print(s.find('r'))


# All checks cannot include space
new_s = "helloworld"
# Is all alphanumeric
print(s.isalnum())
print(f'new_s should be alphanumeric {new_s.isalnum()}')

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())

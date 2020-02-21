# A variable is a container for values which could be multiple types

'''
This could be defined as functions
Or also can be defined as mulilines comments
'''

"""
this can also be defined as comments
Variable rules for python
- Variables are case sensitive(name and NAME are different)
- Must start with a letter or underscore
- Can have numbers but they cannot start with numbers
"""
# No semicolons in python and also no need to define a type
# x = 1          # int by default
# y = 2.5        # float
# name = 'Jhon'  # string
# is_cool = True # boolean must have capital T or capital F

#muliple assignments
x, y, name, is_cool = (1, 2.5, 'Jhon', True)

#Basic Math
a = x + y

#Casting
x = str(x)
y = int(y)
 
# print('Hello')
# print(x)
# print(x, y, name, is_cool, a)
# print(type(x))
print(type(y), y)



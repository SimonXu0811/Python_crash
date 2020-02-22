# A function is a block of codes which will only runs when it is called. In python, we don not use curly brackets, we use indentation with tabs or spaces

# Create function
def sayHello(name):
    print(f'Hello {name}')

# sayHello('Jhon Doe')

def getSum(num1,num2):
    res = num1 + num2
    return res

# print(getSum(1,3))


# A lambda function is a small anonymous function
# A lambda function ca n take any number of arguments, but can only have one expression. Very similar to JS arrow function

getSum = lambda num1, num2 : num1 + num2

num = getSum(2, 4)
print(num)
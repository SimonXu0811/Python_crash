# Python has functions to creating, reading, updating and deleting files

# Open a file
myFile = open('myFile.txt', 'w')

# Get some info
print('Name: ' , myFile.name)
print('Is closed: ' , myFile.closed)
print('Mode: ' , myFile.mode) 

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file
myFile = open('myFile.txt', 'a')
myFile.write(' and also Java')
myFile.close()

# Read from file
myFile = open('myFile.txt', 'r+')
text = myFile.read(100)
print(text)
# This is the finger exercise of 2.2 in book
# Introduction to Computation and Programming Using Python
# Write a program that examines three variables and prints the 
# largest odd number among them.

# Ask the user to enter 3 integers
x = int(input('Please enter an integer x: '))
y = int(input('PLease enter an integer y: '))
z = int(input('Please enter an integer z: '))

oddNumbers = []

# Add x to the oddNumber list if it is an odd number
if x % 2 != 0:
    oddNumbers.append(x)
if y % 2 != 0:
    oddNumbers.append(y)
if z % 2 != 0:
    oddNumbers.append(z)

# If there is no odd number then print the message to inform the users
if len(oddNumbers) == 0:
    print('All three numbers are even numbers')
else:
    oddNumbers.sort() # Sort the odd numbers in the list in the assending order
    print(oddNumbers[-1], 'is the largest odd number')
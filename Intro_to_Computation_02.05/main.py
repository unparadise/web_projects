# This is the finger exercise of 2.5 in book
# Introduction to Computation and Programming Using Python
# Write a program that examines ten variables and prints the 
# largest odd number among them. If there is no odd numbers,
# let the users know.

# Ask the user to enter 3 integers
allNumbersStr = input('Please enter 10 integers separated by comma: ')

# TODO: Add logic to check whether the user has entered more than 10 numbers

allNumbersStrList = allNumbersStr.split(',')

oddNumbers = []

i = 0
while i < len(allNumbersStrList):
    # Add the number to the oddNumber list if it is an odd number
    if int(allNumbersStrList[i]) % 2 != 0:
        oddNumbers.append(int(allNumbersStrList[i]))
    i += 1

# If there is no odd number then print the message to inform the users
if len(oddNumbers) == 0:
    print('All three numbers are even numbers')
else:
    oddNumbers.sort() # Sort the odd numbers in the list in the assending order
    print('-----------------------------------')
    print(oddNumbers[-1], 'is the largest odd number')
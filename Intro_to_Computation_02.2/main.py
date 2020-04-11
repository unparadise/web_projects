# This is the finger exercise of 2.2 in book
# Introduction to Computation and Programming Using Python
# Write a program that examines three variables and prints the 
# largest odd number among them.

x = int(input('Please enter an integer x: '))
y = int(input('PLease enter an integer y: '))
z = int(input('Please enter an integer z: '))

if x > y and x > z and x % 2 != 0:
    if x%2 != 0:
        print(x, ' is the largest odd number')
    else:
        print(x, ', the largest number is not an odd number')
elif y > x:
    if y%2 != 0:
        print(y, ' is the largest odd number')
    else:
        print(y, ', the largest number is not an odd number')
else:
    if z%2 != 0:
        print(z, ' is the largest odd number')
    else:
        print(z, ', the largest number is not an odd number')


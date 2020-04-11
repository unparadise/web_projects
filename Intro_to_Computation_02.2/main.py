# This is the finger exercise of 2.2 in book
# Introduction to Computation and Programming Using Python
# Write a program that examines three variables and prints the 
# largest odd number among them.

x = int(input('Please enter an integer x: '))
y = int(input('PLease enter an integer y: '))
z = int(input('Please enter an integer z: '))

if x > y and x > z:
    if x%2 != 0:
        print(x, ' is the largest odd number')
elif y > x and y > z:
    if y%2 != 0:
        print(y, ' is the largest odd number')
else:
    if z%2 != 0:
        print(z, ' is the largest odd number')

# Decide whether all 3 nubmers are even
if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print('All three numbers are even numbers')

# This is the finger exercise of 3.1 in book
# Introduction to Computation and Programming Using Python
# Write a program that asks the user to enter an integer and
# prints two integers, root and pwr, such that 0 < pwr < 6
# and root**pwr is equal to the integer entered by the user.
# If no such pair of integers exists, it should print a
# message to that effect.

number = int(input('Please enter an integer: '))
# print(number)

root = 1
pwr = 1

while pwr < 6:
    if root**pwr >= number:
        break

    pwr += 1
    root += 1

print(root, '**', pwr, '=', number)
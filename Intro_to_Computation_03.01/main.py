# This is the finger exercise of 3.1 in book
# Introduction to Computation and Programming Using Python
# Write a program that asks the user to enter an integer and
# prints two integers, root and pwr, such that 0 < pwr < 6
# and root**pwr is equal to the integer entered by the user.
# If no such pair of integers exists, it should print a
# message to that effect.

number = int(input('Please enter an integer: '))
# print(number)

root = 0
pwr = 0

while True:
	print('root = ', root)
	print('root ** pwr = ', root ** pwr)
	pwr += 1
	print('pwr = ', pwr)

	if pwr == 6:
		root += 1
		pwr = 0

	if root ** pwr == number:
		print(root, '**', pwr, '=', number)
		break
	elif root == number:
		print('Can\'t find the root and pwr for', number)
		break

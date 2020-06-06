# Implement a function that meets the specification below.
# Use a try-except block.

def sumDigits(s):
	""" Assumes s is a string
		Returns the sum of the decimal digits in s
			For example, if s is 'a2b3c' it returns 5"""

	total = 0

	
	for c in s:
		try:
			total += int(c)
	
		except ValueError:

			print(c, 'is not an integer')

	return total


userString = input('Please enter a string with numbers in it: ')

print('The sum of the decimal digits in', userString, 'is', sumDigits(userString))

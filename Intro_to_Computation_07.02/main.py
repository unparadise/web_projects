# Implement a function that satisfies the specification

def findAnEven(L):
	""" Assumes L is a list of integers
		Returns the first even number in L
		Raises ValueError if L does not contain an even number"""

	for n in L:
		if n%2 == 0:
			return n

	raise Exception('List does not contain an even number')


userString = input('Please enter a list of numbers separated by , :')
l = userString.split(',')

# Convert the items in the string to integers
map_object = map(int, l)
l2 = list(map_object)

# The program does not handle user inputs that do not follow
# the n1, n2, n3...

print(l2)
print(findAnEven(l2))

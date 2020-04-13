# This is the finger exercise in Chapter 2.4 (Iteration)

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''

while(numXs > 0):
    toPrint += 'X'
    numXs -= 1
print(toPrint)
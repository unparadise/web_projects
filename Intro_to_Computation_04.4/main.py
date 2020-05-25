# This is the example code in Chapter 4.4
# The code demonstrate using a global variable
# to track the number of times the fibonacci
# function is called

def fib(x):
    """ Assume x is an integer and >= 0
    Returns Fibonacci of X"""

    global numFibCalls
    numFibCalls += 1

    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib (x-2)


def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0

        print('fib of', i, '=', fib(i))
        print('fib called', numFibCalls, 'times')

testFib(3)

# This program evaluate a string entered by the user
# to see whether it is a palindrome using recursion

def toChars(s):
    s = s.lower()
    letters = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            letters = letters + c
    
    return letters


def isPal(s):

    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1: -1])


def isPalindrome(s):
    """Decide whether a string is a palindrome"""

    return isPal(toChars(s))


userString = input('Please enter a string: ')

if isPalindrome(userString):
    print('The string you entered is a palindrome')
else:
    print('The string you entered is not a palindrome')
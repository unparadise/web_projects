# This is function to check whether a string is a
# palindromes. A palindrome is a word, phrase, or
# sequence that reads the same backward as forward,
# e.g., madam or nurses run

def isPalindrome(userString):
    # covert uppercase letters in the string to lowercase letters
    userString = userString.lower()

    stringChars = list(userString)
    for i in stringChars:
    #   print(i)
        if i.isalpha() == False:
            stringChars.remove(i)

    # print(stringChars)
    for i in range(len(stringChars)):
        # Compare the letters at the front and at the end
        if stringChars[i] != stringChars[-i - 1]:
            print('Your string is not a palindrome')
            return
        else:
            print('Your string is a palindrome')
            return

print('This program tells the user whether an entered string is a palindrome or not')
print('----------------------------------------')
userString = input('Please enter a string: ')

isPalindrome(userString)
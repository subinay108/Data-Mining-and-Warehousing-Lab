# WAPP to check string palindrome

s = input('Enter a string: ')

def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

if is_palindrome(s):
    print(s, 'is a palindrome string')
else:
    print(s, 'is not a palindrome string')
# WAPP to Armstrong Number

n = int(input('Enter a number: '))

def calculate_digit_length(n):
    c = 0
    while n > 0:
        c += 1
        n //= 10
    return c

def is_armstrong(n):
    l = calculate_digit_length(n)
    original_n = n
    s = 0
    while n > 0:
        s += (n % 10) ** l
        n //= 10
    
    return original_n == s 


# if is_armstrong(n):
#     print(n , 'is armstrong')
# else:
#     print(n, 'is not armstrong')

for i in range(n):
    if is_armstrong(i):
        print(i)
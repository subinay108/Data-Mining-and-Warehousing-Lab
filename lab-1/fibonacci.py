# WAPP to print the Fibonacci Series

n = int(input('Enter a number: '))

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, ' ', end='')
        a, b = b, a + b

def fibonacci_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f = fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)
    return f

fibonacci(n)

print(fibonacci_recursion(n))
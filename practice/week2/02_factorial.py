def factorial(n):
    if(n == 0):
        print('')
        return 1
    else:
        print(n, end=' ')
        return n * factorial(n - 1)

print(factorial(5))


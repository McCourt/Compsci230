def factorial(n):
    assert(type(n)==int and n >= 0)
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(50))
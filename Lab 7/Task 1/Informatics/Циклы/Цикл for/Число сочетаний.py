def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input())
k = int(input())

Ckn = factorial(n) // (factorial(k) * factorial(n - k))
print(Ckn)

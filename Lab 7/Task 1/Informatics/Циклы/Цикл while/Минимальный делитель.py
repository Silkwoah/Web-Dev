n = int(input())

divisor = 2

while divisor * divisor <= n:
    if n % divisor == 0:
        print(divisor)
        break
    divisor += 1

if divisor * divisor > n:
    print(n)

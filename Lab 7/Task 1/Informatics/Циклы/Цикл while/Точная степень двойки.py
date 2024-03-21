N = int(input())

if N == 1:
    print("YES")
else:
    while N % 2 == 0 and N > 1:
        N //= 2
    if N == 1:
        print("YES")
    else:
        print("NO")

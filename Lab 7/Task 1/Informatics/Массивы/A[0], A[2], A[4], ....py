N = int(input())
array = list(map(int, input().split()))

for i in range(N):
    if i % 2 == 0:
        print(array[i], end=" ")

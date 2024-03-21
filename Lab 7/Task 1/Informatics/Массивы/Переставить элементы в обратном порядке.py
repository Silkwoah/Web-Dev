N = int(input())
array = list(map(int, input().split()))

start = 0
end = N - 1

while start < end:
    array[start], array[end] = array[end], array[start]
    start += 1
    end -= 1

print(*array)

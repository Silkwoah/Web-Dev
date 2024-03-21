def xor(x, y):
    return int((x or y) and not (x and y))

x, y = map(int, input().split())
print(xor(x, y))

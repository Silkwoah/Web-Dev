a = float(input())
n = int(input())

x = 0
y = 1

for i in range(n + 1):
    x += y
    y *= a

print(x)

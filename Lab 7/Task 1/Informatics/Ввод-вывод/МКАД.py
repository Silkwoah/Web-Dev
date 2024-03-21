v = int(input())
t = int(input())

length_MKAD = 109

distance = v * t

if v > 0:
    position = (0 + distance) % length_MKAD
elif v < 0:
    position = (0 - distance) % length_MKAD

print(position)

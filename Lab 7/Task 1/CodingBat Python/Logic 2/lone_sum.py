def lone_sum(a, b, c):
    if a != b and a != c:
        if b != c:
            return a + b + c
        else:
            return a
    elif a == b == c:
        return 0
    elif a == c:
        return b
    elif a == b:
        return c
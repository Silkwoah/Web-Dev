def no_teen_sum(a, b, c):
    def fix_teen(n):
        if n in [13, 14, 17, 18, 19]:
            return 0
        return n

    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)

    return a + b + c
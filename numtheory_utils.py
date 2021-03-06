def extended_gcd(x, y):
    sx = 1 if x > 0 else -1
    x = abs(x)
    sy = 1 if y > 0 else -1
    y = abs(y)
    pa, pb = 1, 0
    a, b = 0, -1
    done = False
    while True:
        m = (pa * x - pb * y) // (a * x - b * y)
        na = pa - m * a
        nb = pb - m * b
        pa, a = a, na
        pb, b = b, nb
        if (a * x - b * y) in (0, 1):
            if (a < 0) and (b < 0):
                if x < y:
                    return (y + a, -x - b, (a * x - b * y))
                else:
                    return (a, -b, (a * x - b * y))
            else:
                if x < y:
                    return (a, -b, (a * x - b * y))
                else:
                    return (a - y, x - b, (a * x - b * y))

# This is basically the kind of calculation that the above function is trying
# to replicate.
#
# 1 * 23 - 0 * 15 = 23
# 1 * 15 - 0 * 23 = 15
# (1 * 23 - 0 * 15) - (1 * 15 - 0 * 23) = 1 * 23 - 1 * 15 = 8
# (1 * 15 - 0 * 23) - (1 * 23 - 1 * 15) = 2 * 15 - 1 * 23 = 7
# (1 * 23 - 1 * 15) - (2 * 15 - 1 * 23) = 2 * 23 - 3 * 15 = 1
# 20 * 15 - 13 * 23 = 1

# 1 * 23 - 0 * 16 = 23
# 1 * 16 - 0 * 23 = 16
# (1 * 23 - 0 * 16) - (1 * 16 - 0 * 23) = 1 * 23 - 1 * 16 = 7
# (1 * 16 - 0 * 23) - 2 * (1 * 23 - 1 * 16) = 3 * 16 - 2 * 23 = 2
# (1 * 23 - 1 * 16) - 3 * (3 * 16 - 2 * 23) = 7 * 23 - 10 * 16 = 1
# 13 * 16 - 9 * 23 = 1

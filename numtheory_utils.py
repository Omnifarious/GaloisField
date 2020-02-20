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


def print_group_table(elements, op):
    width = max(len(str(x)) for x in elements)
    print(f'{" ":{width}} |', end='')
    for a in elements:
        print(f' {a:{width}} |', end='')
    print()
    for a in elements:
        print(f'{a:{width}} |', end='')
        for b in elements:
            result = op(a, b)
            print(f' {result:{width}} |', end='')
        print()


def mult_inverses(a, b):
    am, bm, g = extended_gcd(a, b)
    if g == 0:
        raise ValueError(f"{a} and {b} are not relatively prime.")
    if am < 0:
        am = b + am
    if bm < 0:
        bm = a + bm
    return f"{a} * {am} % {b} == {a * am % b}"\
        f"\n{b} * {bm} % {a} == {b * bm % a}"

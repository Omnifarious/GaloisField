from typing import Any, Callable, TypeVar, Dict, Collection
try:
    import colorama
    import blessings
    nocolors = False
except ModuleNotFoundError:
    nocolors = True

__all__ = [
    'extended_gcd', 'print_group_table', 'mult_inverse', 'print_mult_inverses'
]

def extended_gcd(x: int, y: int):
    """Return a tuple 't' with three elements such that:
    t[0] * x + t[1] * y == t[2]

    t[2] will be either 0 or 1. If it is zero, then x and y are not
    relatively prime. If it is one, then they are.

    This makes use of Euclid's algorithm for finding the GCD, but extends it
    to keep track of the extra data returned in t[0] and t[1].

    GCD = Greatest Common Denominator
    """
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

T = TypeVar('T')
def print_group_table(
        elements: Collection[T],
        op: Callable[[T, T], T],
        highlight_map: Dict[T, int] = {}
):
    if not nocolors:
        colorama.init()
        term = blessings.Terminal()
    width = max(len(str(x)) for x in elements)
    print(f'{" ":{width}} |', end='')
    def element_str(a, width):
        s = f'{a:{width}}'
        spaces = ' ' * (len(s) - len(str(a)))
        if (not nocolors) and (a in highlight_map):
            return spaces + term.color(highlight_map[a])(str(a))
        else:
            return s
    for a in elements:
        print(f' {element_str(a, width)} |', end='')
    print()
    for a in elements:
        print(f'{element_str(a, width)} |', end='')
        for b in elements:
            result = op(a, b)
            print(f' {element_str(result, width)} |', end='')
        print()


def mult_inverse(a: int, b: int):
    """If possible, return a number n such that a * n mod b == 1, otherwise
    raise an exception."""
    am, bm, g = extended_gcd(a, b)
    if g == 0:
        raise ValueError(f"{a} and {b} are not relatively prime.")
    return am if am > 0 else b + am


def print_mult_inverses(a: int, b: int):
    """Prints out the multiplicative inverse of a (mod b) and the multiplicative
    inverse of b (mod a).
    """
    am, bm, g = extended_gcd(a, b)
    if g == 0:
        raise ValueError(f"{a} and {b} are not relatively prime.")
    if am < 0:
        am = b + am
    if bm < 0:
        bm = a + bm
    print(f"{a} * {am} % {b} == {a * am % b}"\
          f"\n{b} * {bm} % {a} == {b * bm % a}")

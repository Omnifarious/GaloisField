def gen_randomized_fib(r):
    oldest = 1
    older = 1
    bitpool = 0
    bitpoolbits = 0
    while True:
        if bitpoolbits <= 0:
            bitpool = r.getrandbits(64)
            bitpoolbits = 64
        yield oldest
        if (bitpool & 1) == 0:
            oldest, older = older, older + oldest
        else:
            oldest, older = older, older - oldest
        bitpool >>= 1
        --bitpoolbits


def inewt(b, n):
    newest = b >> (b.bit_length() - (b.bit_length() // n))
    est = 0
    while newest != est:
        prevest = est
        est = newest
        newest = ((n - 1) * est + b // (est ** (n - 1))) // n
        if prevest == newest:
            return min(est, newest)
    return newest


def factors(n):
    factors = []
    while n & 1 == 0:
        factors.append(2)
        n = n >> 1
    test = 3
    testsq = 9
    while testsq <= n:
        if (n % test) == 0:
            factors.append(test)
            n = n // test
        else:
            testsq += 4 * test + 4
            test += 2
    factors.append(n)
    return factors


import math


def nth_root_big(b, n):
    if b.bit_length() <= 1023:
        return math.pow(b, 1/n)
    d, m = divmod(b.bit_length(), 1023)
    chop_factor = d + (0 if m == 0 else 1)
    if n < chop_factor:
        raise OverflowError(f"The {n} root of {b} is out of the range of a floating point.")
    flist = factors(n)
    flist.reverse()
    runprod = 1
    while (len(flist) > 0) and (runprod < chop_factor):
        runprod *= flist.pop()
    return math.pow(inewt(b, runprod), 1 / (n // runprod))


from fractions import Fraction as F


def ratpi(n):
    """I have no better place to put this. This is a quickly converging series
    for computing a rational approximation of pi. For when you want more
    precision than math.pi will give you."""
    return sum(F(1/16**k)*(F(4,8*k+1) - F(2,8*k + 4) - F(1,8*k+5) - F(1, 8*k+6)) for k in range(0, n))

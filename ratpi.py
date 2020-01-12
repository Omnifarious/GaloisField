from fractions import Fraction as F

"""I have no better place to put this. This is a quickly converging series for
computing a rational approximation of pi. For when you want more precision
than math.pi will give you."""

def ratpi(n):
    return sum(F(1/16**k)*(F(4,8*k+1) - F(2,8*k + 4) - F(1,8*k+5) - F(1, 8*k+6)) for k in range(0, n))

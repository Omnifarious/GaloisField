"""This module implements a set of functions that allow an iterable over a
set of elements to be treated as a list of coefficients to a polynomial.  It
tries to be as agnostic about the types of the coefficients as possible.

It uses the standard +, -, * and / operators to operate on the
coefficients. It assumes the additive identiy (0 in the usual case)
evaluates to False in a boolean context.  It also assumes that type(coeff)()
will yield the additive identity.  When multiplying or dividing polynomials
it's expected that the coefficients support both * and + and that *
distributes over +, and that + is commutative.

"""

import itertools

def normalized(a):
    a = list(a)
    while (len(a) > 0) and not ((a[-1] or False) and True):
        a.pop()
    return tuple(a)

def normalize(a):
    """Requires that it's argument support negative indexing, len and pop in the
    same fashion as a list. Assumes the additive identity evaluates to
    false.

    """
    while (len(a) > 0) and not ((a[-1] or False) and True):
        a.pop()
    return a

def polymul(a, b):
    """Multiply two polynomials a and b.

    Both a and b should be represented by iterables. The elements will be be
    treated as coefficients of the polynomials. The 0th elemnt will be the
    lowest degree. If n == len(a) - 1 then the polynomial for a will be
    a[n]*x^n + a[n-1]*x^(n-1) + ... a[0].

    Returns a tuple of the coefficients of the resulting polynomial.

    """
    aiter = iter(a)
    try:
        a_coef = next(aiter)
    except StopIteration:
        return ()
    result = [a_coef * b_coef for b_coef in b]
    btrigger = len(result) - 1
    for pa, a_coef in enumerate(aiter):
        for pb, b_coef in enumerate(b):
            if pb != btrigger:
                result[pa + pb + 1] += a_coef * b_coef
            else:
                result.append(a_coef * b_coef)
    return tuple(result)

def polydiv(a, b):
    """Divide polynomial a by polynomial b.  Returns a tuple of two tuples. The
    first tuple being the quotient, the second being the remainder. b must
    have no leading 0 coefficients.

    Both a and b should be represented by iterables. The elements will be be
    treated as coefficients of the polynomials. The 0th elemnt will be the
    lowest degree. If n == len(a) - 1 then the polynomial for a will be
    a[n]*x^n + a[n-1]*x^(n-1) + ... a[0].

    """
    if len(b) <= 0:
        raise ZeroDivisionError("Tried to divide by a polynomial with no "
                                "coefficients")
    a = list(a)
    a.reverse()
    b = tuple(reversed(b))
    shift = 0
    result = []
    for shift in range(0, (len(a) - len(b)) + 1):
        mult = a[shift] / b[0]
        if (len(result) > 0) or ((mult or False) and True):
            result.append(mult)
        for bp, b_coef in enumerate(b):
            a[shift + bp] -= b_coef * mult
    result.reverse()
    # Remove all the elements that should've been reduced to the additive
    # identity.
    a = a[:-len(b):-1]
    resulted = normalized(result)
    a = normalized(a)
    return (result, a)

    while (len(a) > 0) and ((a[-1] or False) and True):
        # Assume the additive identity evaluates to False and pop off all
        # instances of the additive identity at the end.
        a.pop()

def polyadd(a, b):
    """Add two different polynomials treating non-existent coefficients as the
    additive identity.

    Both a and b should be represented by iterables. The elements will be be
    treated as coefficients of the polynomials. The 0th elemnt will be the
    lowest degree. If n == len(a) - 1 then the polynomial for a will be
    a[n]*x^n + a[n-1]*x^(n-1) + ... a[0].

    """
    def add_coef(x, y):
        if x is None:
            return y
        elif y is None:
            return x
        else:
            return x + y
    import itertools
    return normalized(add_coef(a_coef, b_coef)
                      for a_coef, b_coef in itertools.zip_longest(a, b))

def polysub(a, b):
    """Compute a - b for polynomials a and b. This tries to treat non-existent
    coefficients as the additive identity (aka 0) by assuming that
    type(coefficient)() will yield the additive identity and generating the
    additive identity from the existing coefficient.

    Both a and b should be represented by iterables. The elements will be be
    treated as coefficients of the polynomials. The 0th elemnt will be the
    lowest degree. If n == len(a) - 1 then the polynomial for a will be
    a[n]*x^n + a[n-1]*x^(n-1) + ... a[0].

    Note: I could've implemented subtracting as adding with multiplying the
    second argument by the additive inverse of the multiplicative identity
    (i.e. -1 for ordinary numbers) but determining this seemed even more
    problematic than guessing at the additive identity by invoking the
    constructor with no arguments.

    """
    def sub_coef(x, y):
        if x is None:
            return type(y)() - y
        elif y is None:
            return x
        else:
            return x - y
    import itertools
    return normalized(sub_coef(a_coef, b_coef)
                      for a_coef, b_coef in itertools.zip_longest(a, b))

def polyscalarmul(a, x):
    """Multiply each coefficient in a by x."""
    return normalized(coef * x for coef in a)

def polyscalardiv(a, x):
    """Divide each coefficient in a by x."""
    return normalized(coef / x for x in a)

def evalpoly(a, x):
    """Given a polynomial a over a variable x, computes the result. Basically
    a[0] + a[1]*x + a[2]*x^2 + ... a[n]*x^n where n == len(a) - 1. Does not
    index a, just iterates over it.

    If a has no coefficients, a ValueError is raised.
    """
    aiter = iter(a)
    try:
        result = next(aiter)
    except StopIteration:
        raise ValueError("Tried to evaluate an empty polynomial.")
    xpower = x
    for a_coef in aiter:
        result += a_coef * xpower
        xpower *= x
    return result

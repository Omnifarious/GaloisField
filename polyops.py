def polymul(a, b):
    """Multiply two polynomials a and b. Both a and b should be represented by
    iterables. The elements will be be treated as coefficients of the
    polynomials. The 0th elemnt will be the lowest degree. If n == len(a) -
    1 then the polynomial for a will be a[n]*x^n + a[n-1]*x^(n-1) +
    ... a[0].

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
    first tuple being the quotient, the second being the remainder.

    """
    raise NotImplementedError()

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

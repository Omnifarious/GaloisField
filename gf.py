from functools import total_ordering as _total_ordering

class _gfBase(object):
    __slots__ = ('__weakref__')

_fieldTypes = {}

def gfMeta(prime, basis):
    global _fieldTypes
    prime = int(prime)
    basis = tuple((int(p) for p in basis))
    tmpclass = _fieldTypes.get((prime, basis))
    if tmpclass is not None:
        return tmpclass
    del tmpclass

    for p in basis:
        if (p < 0) or (p >= prime):
            raise ValueError("Each element of basis must be >= 0 "
                             "and < prime.")
    if basis[0] != 1:
        raise ValueError("First element of basis must be 1")
    size = len(basis) - 1

    @_total_ordering
    class gf(_gfBase):
        __slots__ = ('val_')
        prime_ = prime
        basis_ = basis

        def __init__(self, val):
            val = tuple((int(v) for v in val))
            if len(val) != size:
                raise ValueError("val must be sequence of size size of ints")
            if any((v < 0) or (v >= prime) for v in val):
                raise ValueError("Each element of val must be >= 0 and < %d"
                                 % (prime,))
            self.val_ = val
            super().__init__()

        def __eq__(self, other):
            if not isinstance(other, _gfBase):
                return NotImplemented
            elif other.prime_ != self.prime_:
                return NotImplemented
            elif other.basis_ != self.basis_:
                return NotImplemented
            else:
                return self.val_ == other.val_

        def __lt__(self, other):
            if not isinstance(other, _gfBase):
                return NotImplemented
            elif other.prime_ != self.prime_:
                return NotImplemented
            elif other.basis_ != self.basis_:
                return NotImplemented
            else:
                return self.val_ < other.val_

        def __repr__(self):
            return "<%s.%s(%d, %r)(%r)>" % \
                (gfMeta.__module__, gfMeta.__qualname__,
                 prime, basis, self.val_)

    _fieldTypes[(prime, basis)] = gf
    return gf

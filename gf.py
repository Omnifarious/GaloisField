from functools import total_ordering as _total_ordering

class _gfBase(object):
    __slots__ = ('__weakref__')

_fieldTypes = {}

def gfMeta(prime_, basis_):
    global _fieldTypes
    prime_ = int(prime_)
    basis_ = tuple((int(p) for p in basis_))
    tmpclass = _fieldTypes.get((prime_, basis_))
    if tmpclass is not None:
        return tmpclass
    del tmpclass

    for p in basis_:
        if (p < 0) or (p >= prime_):
            raise ValueError("Each element of basis must be >= 0 "
                             "and < prime.")
    if basis_[0] != 1:
        raise ValueError("First element of basis must be 1")
    size_ = len(basis_) - 1

    @_total_ordering
    class gf(_gfBase):
        __slots__ = ('val_')

        @property
        def prime(self):
            "The prime number field for each element of the Galois Field."
            return prime_

        @property
        def basis(self):
            "The coefficients of the prime polynomial defining the field."
            return basis_

        def __init__(self, val):
            val = tuple((int(v) for v in val))
            if len(val) != size_:
                raise ValueError("val must be sequence of size size_ of ints")
            if any((v < 0) or (v >= prime_) for v in val):
                raise ValueError("Each element of val must be >= 0 and < %d"
                                 % (prime_,))
            self.val_ = val
            super().__init__()

        def _compat_types(self, other):
            return isinstance(other, _gfBase) \
                and (other.prime == prime_) \
                and (other.basis == basis_)

        def __eq__(self, other):
            return (self.val_ == other.val_) \
                if self._compat_types(other) else NotImplemented

        def __neq__(self, other):
            return (self.val_ != other.val_) \
                if self._compat_types(other) else NotImplemented

        def __lt__(self, other):
            return (self.val_ < other.val_) \
                if self._compat_types(other) else NotImplemented

        def __repr__(self):
            return "<%s.%s(%d, %r)(%r)>" % \
                (gfMeta.__module__, gfMeta.__qualname__,
                 prime_, basis_, self.val_)

        def __str__(self):
            return "[: " + ' '.join(str(v) for v in self.val_) + " :]"

        def __add__(self, other):
            if not self._compat_types(other):
                return NotImplemented
            return self.__class__((((x + y) % prime_) for (x, y) in \
                                      zip(self.val_, other.val_)))

        def __sub__(self, other):
            if not self._compat_types(other):
                return NotImplemented
            return self.__class__((((x + (prime_ - y)) % prime_) \
                                       for (x, y) in \
                                       zip(self.val_, other.val_)))

        def _intmul(self, other):
            if other == 0:
                return self.__class__([0] * size_)
            elif other < 0:
                return self.__class__([0] * size_) - self._intmul(-other)
            elif other & 1:
                return self + self._intmul(other - 1)
            else:
                tmp = self._intmul(other // 2)
                return tmp + tmp

        def __mul__(self, other):
            if not self._compat_types(other):
                try:
                    other = int(other)
                except:
                    pass
                if isinstance(other, int):
                    return self._intmul(other)
                else:
                    return NotImplemented
            tmpval = [0] * (size_ * 2)
            for i, factor in enumerate(reversed(other.val_)):
                for j, term in enumerate(reversed(self.val_)):
                    tmpval[i + j] += factor * term
            tmpval = tuple((term % prime_) for term in tmpval)
            tmpval = tuple(reversed(tmpval))
            shiftval = tuple((prime_ - term) % prime_ for term in basis_) \
                + ((0,) * (size_ - 1))
            while len(tmpval) > size_:
                while tmpval[0] != 0:
                    tmpval = tuple((x + y) % prime_ \
                                       for x, y in zip(tmpval, shiftval))
                tmpval = tmpval[1:]
                shiftval = shiftval[:-1]
            return self.__class__(tmpval)

        def __rmul__(self, other):
            if not self._compat_types(other):
                try:
                    other = int(other)
                except:
                    pass
                if isinstance(other, int):
                    return self._intmul(other)
                else:
                    return NotImplemented
            return NotImplemented

        def __pow__(self, other):
            try:
                other = int(other)
            except TypeError:
                return NotImplemented
            if other < 0:
                raise ValueError("Negative powers are not supported.")
            start = self.__class__((0,) * (size_ - 1) + (1,))
            base = self
            while other > 0:
                if other & 1:
                    start = start * base
                base = base * base
                other >>= 1
            return start

        def __bool__(self):
            return any(x != 0 for x in self.val_)

        def __hash__(self):
            return hash((prime_, basis_, self.val_))

    _fieldTypes[(prime_, basis_)] = gf
    return gf

def generate_field(start):
    cur = start ** 0
    vals = set()
    field = []
    while cur not in vals:
        field.append(cur)
        vals.add(cur)
        cur = cur * start
    return field

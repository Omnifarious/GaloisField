def gfMeta(prime, basis):
    prime = int(prime)
    basis = tuple((int(p) for p in basis))
    for p in basis:
        if (p < 0) or (p >= prime):
            raise ValueError("Each element of basis must be >= 0 "
                             "and < prime.")
    if basis[0] != 1:
        raise ValueError("First element of basis must be 1")
    size = len(basis)

    class gf(type):
        def __init__(self, val):
            val = tuple((int(v) for v in val))
            if len(val) != size:
                raise ValueError("val must be sequence of size size of ints")
            self.val_ = val_

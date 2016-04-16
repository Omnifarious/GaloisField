import collections

def generate(p, b=2):
    m = 1
    while m < p:
        m *= 2
    m = m // 2
    d = []
    s = 1
#    print(s, m)
    generated = set()
    while s not in generated:
#        print(len(d), s)
        d.append(s)
        generated.add(s)
        s *= b
        while s >= m:
            tmp = p << (s.bit_length() - p.bit_length())
#            print(s, tmp)
            s ^= tmp
    return d

class testit(object):
    def __init__(self, *args, **kargs):
        print("__init__(args = %s, kargs = %s)" % (repr(args), repr(kargs)))
    def __getattr__(self, *args, **kargs):
        print("__getattr__(args = %s, kargs = %s)" % (repr(args), repr(kargs)))
        return None
    def __prepare__(self, *args, **kargs):
        print("__prepare__(args = %s, kargs = %s)" % (repr(args), repr(kargs)))
        return None
    def __call__(self, *args, **kargs):
        print("__call__(args = %s, kargs = %s)" % (repr(args), repr(kargs)))
        return object()

import polyops
import fractions
from functools import reduce

xlst = [1, 2, 3, 7, 12]
ylst = [9, 10, 5, 4, 1]

master_poly = reduce(polyops.polymul, ((-x, 1) for x in xlst), (1,))
master_poly = polyops.polyscalarmul(master_poly, fractions.Fraction(1, 1))
xpolys = [polyops.polydiv(master_poly, (-x, 1))[0] for x in xlst]
xpolys = [polyops.polyscalarmul(xp, y / polyops.evalpoly(xp, x))
          for xp, x, y in zip(xpolys, xlst, ylst)]
interp = reduce(polyops.polyadd, xpolys, ())

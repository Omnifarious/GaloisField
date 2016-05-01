# <gf.gfMeta(5, (1, 4, 1, 4, 1, 4, 1))((0, 0, 0, 0, 1, 3))>
# (%i58) p2;p3;p4;p5;p6;p7;
# Evaluation took 0.0000 seconds (0.0000 elapsed)
#                                      15
# (%o58)                              x   - x
# Evaluation took 0.0000 seconds (0.0000 elapsed)
#                          6    5    4      3      2
# (%o59)                  x  + x  + x  + 2 x  + 4 x  + 3
# Evaluation took 0.0000 seconds (0.0000 elapsed)
#                             6    5      2
# (%o60)                     x  + x  + 2 x  + 4 x + 4
# Evaluation took 0.0000 seconds (0.0000 elapsed)
#                       6      5    4      3    2
# (%o61)               x  + 4 x  + x  + 4 x  + x  + 4 x + 2
# Evaluation took 0.0000 seconds (0.0000 elapsed)
#                            6      5      4      2
# (%o62)                    x  + 4 x  + 4 x  + 4 x  + 1
# Evaluation took 0.0000 seconds (0.0000 elapsed)
#                       6    5    4      3      2
# (%o63)               x  + x  + x  + 3 x  + 3 x  + 3 x + 4


def gen_groups(l, prime):
    size = len(l)
    yield (0,)
    members = set((0,))
    for i in range(0, len(l)):
        if i in members:
            continue
        group = []
        member = i
        while member not in group:
            group.append(member)
            members.add(member)
            member = member * prime % size
        yield tuple(group)

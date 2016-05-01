# <gf.gfMeta(5, (1, 4, 1, 4, 1, 4, 1))((0, 0, 0, 0, 1, 3))>

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

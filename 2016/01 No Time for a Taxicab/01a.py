# mkaneshiro
# 2023-12-08
# Advent of Code 2016
# Day 1: No Time for a Taxicab, Part 1

with open("input.txt", "r") as f:
    inps = f.read().splitlines()[0].split(", ")

def solve(pzl):
    loc = (0, 0)
    dcounter = 0  # 0 = North, 1 = East, 2 = South, 3 = West
    for inst in pzl:
        d = inst[0]
        l = int(inst[1:])
        if d == "L":
            dcounter -= 1
        else:
            dcounter += 1

        if dcounter % 4 == 0:
            loc = addTup(loc, (0, l))
        elif dcounter % 4 == 1:
            loc = addTup(loc, (l, 0))
        elif dcounter % 4 == 2:
            loc = addTup(loc, (0, -l))
        else:
            loc = addTup(loc, (-l, 0))
    x, y = loc
    return abs(x) + abs(y)

def addTup(orig, new):
    return tuple([orig[i] + new[i] for i in range(len(orig))])

print(solve(inps))

# Answer: 279

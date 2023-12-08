# mkaneshiro
# 2023-12-08
# Advent of Code 2016
# Day 1: No Time for a Taxicab, Part 1

with open("input.txt", "r") as f:
    inps = f.read().splitlines()[0].split(", ")

def solve(pzl):
    loc = (0, 0)
    dcounter = 0  # 0 = North, 1 = East, 2 = South, 3 = West
    locDict = {loc:1}
    for inst in pzl:
        d = inst[0]
        l = int(inst[1:])
        if d == "L":
            dcounter -= 1
        else:
            dcounter += 1

        if dcounter % 4 == 0:
            oldcoord = loc[1]
            loc = addTup(loc, (0, l))
            for i in range(1, l+1):
                if addTup((loc[0], oldcoord), (0, i)) in locDict:
                    return sum([abs(j) for j in addTup((loc[0], oldcoord), (0, i))])
                else: locDict[addTup((loc[0], oldcoord), (0, i))] = 1
        elif dcounter % 4 == 1:
            oldcoord = loc[0]
            loc = addTup(loc, (l, 0))
            for i in range(1, l+1):
                if addTup((oldcoord, loc[1]), (i, 0)) in locDict:
                    return sum([abs(j) for j in addTup((oldcoord, loc[1]), (i, 0))])
                else: locDict[addTup((oldcoord, loc[1]), (i, 0))] = 1
        elif dcounter % 4 == 2:
            oldcoord = loc[1]
            loc = addTup(loc, (0, -l))
            for i in range(1, l+1):
                if addTup((loc[0], oldcoord), (0, -i)) in locDict:
                    return sum([abs(j) for j in addTup((loc[0], oldcoord), (0, -i))])
                else: locDict[addTup((loc[0], oldcoord), (0, -i))] = 1
        else:
            oldcoord = loc[0]
            loc = addTup(loc, (-l, 0))
            for i in range(1, l+1):
                if addTup((oldcoord, loc[1]), (-i, 0)) in locDict:
                    return sum([abs(j) for j in addTup((oldcoord, loc[1]), (-i, 0))])
                else: locDict[addTup((oldcoord, loc[1]), (-i, 0))] = 1


def addTup(orig, new):
    return tuple([orig[i] + new[i] for i in range(len(orig))])

print(solve(inps))

# Answer: 

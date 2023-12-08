# mkaneshiro
# 2023-12-08
# Advent of Code 2016
# Day 2: Bathroom Security, Part 2

with open("input.txt", "r") as f:
    inps = f.readlines()

def solve(pzl):
    grid = [[None, None, '1', None, None], [None, '2', '3', '4', None], ['5', '6', '7', '8', '9'], [None, 'A', 'B', 'C', None], [None, None, 'D', None, None]]
    pointer = (2, 0)
    code = ""
    for num in pzl:
        for d in num:
            if d == "U":
                pointer = addTup(pointer, (-1, 0), grid)
            elif d == "L":
                pointer = addTup(pointer, (0, -1), grid)
            elif d == "R":
                pointer = addTup(pointer, (0, 1), grid)
            elif d == "D":
                pointer = addTup(pointer, (1, 0), grid)
        code += grid[pointer[0]][pointer[1]]
    return code


def addTup(orig, new, grid):
    res = [orig[i] + new[i] for i in range(len(orig))]
    if 0 <= res[0] < len(grid):
        if 0 <= res[1] < len(grid[res[0]]):
            if grid[res[0]][res[1]]:
                return tuple(res)
            else: return orig
        else:
            return orig
    else:
        return orig


print(solve(inps))

# Answer: 659AD

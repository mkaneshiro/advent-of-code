# mkaneshiro
# 2023-12-08
# Advent of Code 2016
# Day 2: Bathroom Security, Part 1

with open("input.txt", "r") as f:
    inps = f.readlines()

def solve(pzl):
    grid = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    pointer = (1, 1)
    code = ""
    for num in pzl:
        for d in num:
            if d == "U":
                pointer = addTup(pointer, (-1, 0))
            elif d == "L":
                pointer = addTup(pointer, (0, -1))
            elif d == "R":
                pointer = addTup(pointer, (0, 1))
            elif d == "D":
                pointer = addTup(pointer, (1, 0))
        code += grid[pointer[0]][pointer[1]]
        print(code)
    return code


def addTup(orig, new):
    res = [orig[i] + new[i] for i in range(len(orig))]
    if 0 <= res[0] <= 2 and 0 <= res[1] <= 2:
        return tuple(res)
    else:
        return orig


print(solve(inps))

# Answer: 47978

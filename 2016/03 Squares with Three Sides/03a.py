# mkaneshiro
# 2023-12-08
# Advent of Code 2016
# Day 3: Squares with Three Sides, Part 1

with open("input.txt", "r") as f:
    inps = f.read().splitlines()

def possible(sidearr):
    sidearr = [int(i) for i in sidearr]
    upper = max(sidearr)
    lower = min(sidearr)

    if upper < sum(sidearr) - upper:
        return True
    return False

def solve(pzls):
    counter = 0
    for pzl in pzls:
        if possible(pzl.split()):
            counter += 1
    return counter

print(solve(inps))

# Answer: 1050

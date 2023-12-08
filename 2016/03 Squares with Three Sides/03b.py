# mkaneshiro
# 2023-12-08
# Advent of Code 2016
# Day 3: Squares with Three Sides, Part 2

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
    pzls = chunk(pzls)
    for pzl in pzls:
        if possible(pzl):
            counter += 1
    return counter

def chunk(pzl):
    fullList = []
    for i in range(len(pzl)):
        if i % 3 == 0:
            for j in range(3):
                fullList.append([pzl[i].split()[j], pzl[i+1].split()[j], pzl[i+2].split()[j]])
    return fullList

print(solve(inps))

# Answer: 1921

# mkaneshiro
# 2023-12-08
# Advent of Code 2023
# Day 8: Haunted Wasteland, Part 2

import re
from numpy import lcm

with open("input.txt", "r") as f:
    inps = f.read().split("\n")

def solve(puz):
    inst = puz[0]
    leftDict = dict()
    rightDict = dict()
    aSet = set()
    zSet = set()
    for line in puz[2:-1]:
        src = re.match(r"[^\s]+", line).group()
        aEnd = re.match(r"[^\s]+A", line)
        if aEnd:
            aSet.add(aEnd.group())
        zEnd = re.match(r"[^\s]+Z", line)
        if zEnd:
            zSet.add(zEnd.group())
        leftDict[src] = re.search(r"\([^\s,]+", line).group()[1:]
        rightDict[src] = re.search(r"[^\s,]+\)", line).group()[:-1]

    pointer = aSet
    cycleList = [cycle(p, inst, leftDict, rightDict) for p in pointer]
    return lcm.reduce(cycleList)


def cycle(point, inst, left, right):
    counter = 0
    while point[-1] != "Z":
        if inst[counter % len(inst)] == "L":
            point = left[point]
        else:
            point = right[point]
        counter += 1
    return counter

print(solve(inps))

# Answer: 10241191004509

# mkaneshiro
# 2023-12-08
# Advent of Code 2023
# Day 8: Haunted Wasteland, Part 1

import re

with open("input.txt", "r") as f:
    inps = f.read().split("\n")

def solve(puz):
    inst = puz[0]
    leftDict = dict()
    rightDict = dict()
    for line in puz[2:-1]:
        src = re.match(r"[^\s]+", line).group()
        leftDict[src] = re.search(r"\([^\s,]+", line).group()[1:]
        rightDict[src] = re.search(r"[^\s,]+\)", line).group()[:-1]

    point = "AAA"
    counter = 0
    dest = "ZZZ"

    while point != dest:
        if inst[counter % len(inst)] == "L":
            point = leftDict[point]

        else:
            point = rightDict[point]
        counter += 1
    return counter

            
print(solve(inps))

# Answer: 14893

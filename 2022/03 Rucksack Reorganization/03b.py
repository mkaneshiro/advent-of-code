# mkaneshiro
# 2023-12-02
# Advent of Code 2022
# Day 3: Rucksack Reorganization, Part 2

import numpy as np

with open("input.txt", "r") as f:
    inps = np.array(f.read().splitlines())
    f.close()

groups = np.split(inps, len(inps)//3)

def solve(sacks):
    for item in sacks[0]:
        if item in sacks[1] and item in sacks[2]:
            badge = item
    pristring = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return pristring.index(badge) + 1

print(sum([solve(group) for group in groups]))

# Answer: 2716

# mkaneshiro
# 2023-12-08
# Advent of Code 2016
# Day 4: Security Through Obscurity, Part 1

import collections, re

with open("input.txt", "r") as f:
    inps = f.read().splitlines()

def solve(pzl):
    sectorSum = 0
    for line in pzl:
        checksum = set(re.search(r"\[\D{5}\]", line).group()[1:-1])
        sector = int(re.search(r"\d+", line).group())
        chars = re.match(r"\D+", line).group().replace("-", "")
        c = collections.Counter(chars)
        topfive = pullFive(c)
        if topfive == checksum:
            sectorSum += sector
    return sectorSum


def pullFive(d):
    fiveSet = set()
    for val in sorted(d.values(), reverse=True):
        tempList = sorted([k for k, v in d.items() if v == val])
        toAdd = min(len(tempList), 5-len(fiveSet))
        fiveSet = fiveSet | set([tempList[i] for i in range(toAdd)])
    return fiveSet

print(solve(inps))

# Answer: 409147

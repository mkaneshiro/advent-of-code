# mkaneshiro
# 2023-12-01
# Advent of Code 2023
# Day 1: Trebuchet?!, Part 2

import re

with open("input.txt", "r") as f:
    inpt = f.readlines()
    f.close()

def solve(line):
    numdict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    numstr = "123456789"
    posdict = dict()
    for num in numdict:
        if num in line:
            indobj = re.finditer(num, line)
            inds = [index.start() for index in indobj]
            for i in inds:
                posdict[i] = numdict[num]
    for i in range(len(line)):
        if line[i] in numstr:
            posdict[i] = line[i]
    return int(str(posdict[min(posdict.keys())]) + str(posdict[max(posdict.keys())]))

print(sum([solve(inp) for inp in inpt]))

# Answer: 54649

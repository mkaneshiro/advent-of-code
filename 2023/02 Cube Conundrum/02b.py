# mkaneshiro
# 2023-12-02
# Advent of Code 2023
# Day 2: Cube Conundrum, Part 2

import re

with open("input_1.txt", "r") as f:
    inpt = f.readlines()
    f.close()

def solve(line):
    index = int(re.match(r"Game\ \d+:", line).group(0).split(" ")[1][:-1])
    grabs = line[line.index(":")+1:].split(";")
    bset, rset, gset = set(), set(), set()
    bval, rval, gval = 0, 0, 0
    for g in grabs:
        cols = g.split(",")
        for i in cols:
            if "blue" in i:
                bset.add(int(re.search(r"\d+\ blue", i).group(0)[:i.index(" b")-1]))
            if "red" in i:
                rset.add(int(re.search(r"\d+\ red", i).group(0)[:i.index(" r")-1]))
            if "green" in i:
                gset.add(int(re.search(r"\d+\ green", i).group(0)[:i.index(" g")-1]))
        if len(bset) > 0:
            bval = max(bset)
        if len(rset) > 0:
            rval = max(rset)
        if len(gset) > 0:
            gval = max(gset)
    return bval*rval*gval

output = sum([solve(inp) for inp in inpt])
print(output)

# Answer: 69110

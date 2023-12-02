# mkaneshiro
# 2023-12-01
# Advent of Code 2023
# Day 1: Trebuchet?!, Part 1

import re

with open("input.txt", "r") as f:
    inpt = f.readlines()
    f.close()

def solve(line):
    digits = re.sub(r"[^\d]+", '', line)
    first = digits[0]
    last = digits[-1]
    return int(first+last)

print(sum([solve(inp) for inp in inpt]))

# Answer: 54081

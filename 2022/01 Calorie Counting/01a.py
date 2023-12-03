# mkaneshiro
# 2023-12-02
# Advent of Code 2022
# Day 1: Calorie Counting, Part 1

with open("input.txt", "r") as f:
    inps = f.read().splitlines()
    f.close()

splinps = []
temp = []

for line in inps:
    if line == "":
        splinps.append(temp)
        temp = []
    else:
        temp.append(int(line))

def solve(elves):
    return max([sum(elf) for elf in elves])

print(solve(splinps))

# Answer: 74394

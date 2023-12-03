# mkaneshiro
# 2023-12-02
# Advent of Code 2022
# Day 3: Rucksack Reorganization, Part 1

with open("input.txt", "r") as f:
    inps = f.read().splitlines()
    f.close()

def solve(sack):
    comp1 = sack[:len(sack)//2]
    comp2 = sack[len(sack)//2:]
    
    pristring = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for item in comp1:
        if item in comp2:
            return pristring.index(item) + 1

print(sum([solve(inp) for inp in inps]))

# Answer: 7967

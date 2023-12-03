# mkaneshiro
# 2022-12-02
# Advent of Code 2022
# Day 2: Rock Paper Scissors, Part 1

with open("input.txt", "r") as f:
    inps = f.read().splitlines()
    f.close()

def solve(game):
    points = 0
    op = game[0]
    me = game[2]

    if me == "X":
        points += 1
    elif me == "Y":
        points += 2
    elif me == "Z":
        points += 3
    else: points += 0

    if op == "A":
        if me == "X":
            points += 3
        elif me == "Y":
            points += 6
    elif op == "B":
        if me == "Y":
            points += 3
        elif me == "Z":
            points += 6
    elif op == "C":
        if me == "X":
            points += 6
        elif me == "Z":
            points += 3
    return points

total = sum([solve(inp) for inp in inps])
print(total)

# Answer: 10941

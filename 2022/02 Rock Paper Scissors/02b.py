# mkaneshiro
# 2023-12-02
# Advent of Code 2022
# Day 2: Rock Paper Scissors, Part 2

with open("input.txt", "r") as f:
    inps = f.read().splitlines()
    f.close()

def solve(game):
    points = 0
    op = game[0]
    res = game[2]

    if res == "X":
        if op == "A":
            points += 3
        elif op == "B":
            points += 1
        elif op == "C":
            points += 2
    elif res == "Y":
        if op == "A":
            points += 4
        elif op == "B":
            points += 5
        elif op == "C":
            points += 6
    elif res == "Z":
        if op == "A":
            points += 8
        elif op == "B":
            points += 9
        elif op == "C":
            points += 7
    return points


total = sum([solve(inp) for inp in inps])
print(total)

# Answer: 13071

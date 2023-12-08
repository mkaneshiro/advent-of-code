# mkaneshiro
# 2023-12-08
# Advent of Code 2023
# Day 7: Camel Cards, Part 1

import collections

with open("input.txt", "r") as f:
    inps = f.read().splitlines()

def solve(puz):
    card_conv = "23456789TJQKA"
    total = 0
    ranking = []
    for line in puz:
        hand, bid = line.split()
        ranking.append((value(hand), conversion(hand, card_conv), int(bid)))

    for idx, i in enumerate(sorted(ranking)):
        x, y, b = i
        total += (idx+1) * b
    return total
    

def value(hand):
    counts = collections.Counter(char for char in hand if char)
    most = max(counts.values())
    if most > 3:
        return most + 2
    elif most == 3:
        if min(counts.values()) == 2:
            return most + 2
        else:
            return most + 1
    elif most == 2:
        if len(counts) == 3:
            return most + 1
        else:
            return most
    else:
        return most

def conversion(hand, vals):
    return tuple(vals.index(char) for char in hand)

print(solve(inps))

# Answer: 253603890

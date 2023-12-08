# mkaneshiro
# 2023-12-08
# Advent of Code 2023
# Day 7: Camel Cards, Part 2

import collections

with open("input.txt", "r") as f:
    inps = f.read().splitlines()

def solve(puz):
    card_conv = "J23456789TQKA"
    total = 0
    ranking = []
    for line in puz:
        hand, bid = line.split()
        if "J" not in hand:
            ranking.append((value(hand), conversion(hand, card_conv), int(bid)))
        else:
            ranking.append((joker(hand), conversion(hand, card_conv), int(bid)))

    for idx, i in enumerate(sorted(ranking)):
        x, y, b = i
        total += (idx+1) * b
    return total
    

def value(hand):
    counts = collections.Counter(char for char in hand)
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

def joker(hand):
    counts = collections.Counter(char for char in hand if char != "J")
    numJ = sum([1 for i in hand if i == "J"])
    if not counts.values():
        return 7  # JJJJJ
    most = max(counts.values())
    if len(counts.values()) == 1:
        return 7 #JJJJX
    elif len(counts.values()) == 2:
        if numJ == 1: # JXXYY, JXYYY
            if most == 3:
                return 6
            else:
                return 5
        else:         # JJXYY, JJJXY
            return 6
    elif len(counts.values()) == 3: # JXYZZ, JJXYZ
        return 4
    elif len(counts.values()) == 4: # JXYZA
        return 2


print(solve(inps))

# Answer: 253630098

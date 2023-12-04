# mkaneshiro
# 2023-12-04
# Advent of Code 2023
# Day 4: Scratchcards, Part 1

import re

with open("input.txt", "r") as f:
    inps = f.readlines()

def solve(card):
    rawCard = card[card.index(":")+1:]
    lineInd = card.index("|")
    winList = re.split(r"\s+", card[:lineInd])[2:-1]
    yourList = re.split(r"\s+", card[lineInd+1:])[1:-1]
    outputList = [0] + [2**n for n in range(len(yourList))]
    numList = [num for num in yourList if num in winList]
    return outputList[len(numList)]

result = sum([solve(inp) for inp in inps])
print(result)

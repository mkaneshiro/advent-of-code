# mkaneshiro
# 2023-12-04
# Advent of Code 2023
# Day 4: Scratchcards, Part 2

import re

with open("input.txt", "r") as f:
    inps = f.readlines()

def solve(cards):
    numDict = {c:1 for c in range(len(cards))}
    for i in range(len(cards)):
        card = cards[i]
        rawCard = card[card.index(":")+1:]
        lineInd = card.index("|")
        winList = re.split(r"\s+", card[:lineInd])[2:-1]
        yourList = re.split(r"\s+", card[lineInd+1:])[1:-1]
        outputList = [0] + [2**n for n in range(len(yourList))]
        numList = (set(winList) & set(yourList))
        for newCard in range(len(numList)):
            numDict[i+newCard+1] += numDict[i]
    return sum(numDict.values())
        
print(solve(inps))

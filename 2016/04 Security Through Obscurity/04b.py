# mkaneshiro
# 2023-12-09
# Advent of Code 2016
# Day 4: Security Through Obscurity, Part 2

import collections, re, string

with open("input.txt", "r") as f:
    inps = f.read().splitlines()

def solve(pzl):
    strList = []
    output = []
    for line in pzl:
        checksum = set(re.search(r"\[\D{5}\]", line).group()[1:-1])
        sector = int(re.search(r"\d+", line).group())
        chars = re.match(r"\D+", line).group()
        chars_five = chars.replace("-", "")
        c = collections.Counter(chars_five)
        topfive = pullFive(c)
        if topfive == checksum:
            if "northpole" in decrypted(chars, sector):
                return sector
    
def pullFive(d):
    fiveSet = set()
    for val in sorted(d.values(), reverse=True):
        tempList = sorted([k for k, v in d.items() if v == val])
        toAdd = min(len(tempList), 5-len(fiveSet))
        fiveSet = fiveSet | set([tempList[i] for i in range(toAdd)])
    return fiveSet
            
def decrypted(text, shift):
    output = []
    text = text.replace("-", " ").rstrip()
    alphabet = string.ascii_lowercase
    table = str.maketrans(alphabet, alphabet[shift % 26:] + alphabet[:shift % 26])
    return text.translate(table)

print(solve(inps))

# Answer: 991

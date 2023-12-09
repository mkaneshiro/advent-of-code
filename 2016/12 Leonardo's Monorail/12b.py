# mkaneshiro
# 2023-12-09
# Advent of Code 2016
# Day 12: Leonardo's Monorail, Part 2

with open("input.txt", "r") as f:
    inps = f.read().splitlines()

def solve(pzl):
    pnt = 0
    valDict = {"a":0, "b":0, "c":1, "d":0}
    while pnt < len(pzl):
        read = pzl[pnt].split()
        if read[0] == "cpy":
            cpy(read[1], read[2], valDict)
            pnt += 1
        elif read[0] == "inc":
            inc(read[1], valDict)
            pnt += 1
        elif read[0] == "dec":
            dec(read[1], valDict)
            pnt += 1
        elif read[0] == "jnz":
            pnt = jnz(read[1], read[2], valDict, pnt)
    return valDict["a"]
            

def cpy(x, y, d):
    if x not in d:
        d[y] = int(x)
    else:
        d[y] = d[x]

def inc(x, d):
    d[x] += 1

def dec(x, d):
    d[x] -= 1

def jnz(x, y, d, p):
    if x not in d:
        if x != 0:
            p += int(y)
    elif x in d and d[x] != 0:
            p += int(y)
    else: p += 1
    return p
    
print(solve(inps))

# Answer: 9227647

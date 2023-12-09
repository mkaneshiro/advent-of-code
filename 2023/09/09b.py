# mkaneshiro
# 2023-12-09
# Advent of Code 2023
# Day 9: Mirage Maintenance, Part 2

with open("input.txt", "r") as f:
    inps = f.read().splitlines()

def solve(pzl):
    total = 0
    for line in pzl:
        counter = 0
        arr = [int(num) for num in line.split()]
        lineDict = {0:arr}
        while set(lineDict[counter]) != set([0]):
            arr = lineDict[counter]
            lineDict[counter + 1] = [arr[i] - arr[i-1] for i in range(1, len(arr))]
            counter += 1

        total += backup(lineDict)
    return total

def backup(l):
    start = max(l.keys())
    n = 0
    for i in range(start+1):
        nval = l[start-i][0] - n
        n = nval
        print(nval)
    return nval


print(solve(inps))

# Answer: 1129

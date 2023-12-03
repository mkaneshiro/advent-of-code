# Advent of Code 2022 -- Day 8

content = open("Day8.txt", "r").read().splitlines()

def readtoGrid(lines):
    gridList = []
    for i in lines:
        gridList.append([int(j) for j in list(i)])
    return gridList

glist = readtoGrid(content)

def checkLeft(grid):
    
    for row in grid:
        for i in range(len(row)):
            if grid[row][i] == max(grid[row][:i]):



# Advent of Code 2022 -- Day 1

content = open("Day1.txt", 'r').read().splitlines()

## Part 1
tempList = []
calorieList = []
for i in content:
    if i != '':
        tempList.append(int(i))
    else:
        calorieList.append(sum(tempList))
        tempList = []

print("Greatest number of calories: " + str(max(calorieList)))

## Part 2

calorieList.sort()
totalThree = sum(calorieList[-3:])

print(totalThree)

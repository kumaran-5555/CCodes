__author__ = 'serajago'

# http://www.geeksforgeeks.org/mobile-numeric-keypad-problem/

possibilities = {1: [2, 4], 2: [1, 3, 5], 3: [2, 6], 4: [1, 5, 7], 5: [2, 6, 4, 8], 6: [5, 3, 9], 7: [4, 8],
                 8: [5, 7, 9, 0], 9: [6, 8], 0: [8]}

dpTable = []

# dpTable[i,j] will hold number of possibilities with i as the current position and number of times is j

for i in range(10):
    dpTable.append([-1] * 10)


# initialize
# ignore zero number of times
for i in range(10):
    dpTable[i][0] = 0
    dpTable[i][1] = 1

# sum of dptable[*][k] will give the total possiblities

def printDpTable():
    for i in range(10):
        print(dpTable[i])

def getNumOfPossibilities(currentPos, numOfTimes):
    if dpTable[currentPos][numOfTimes] != -1:
        return dpTable[currentPos][numOfTimes]

    total = 0

    for i in possibilities[currentPos]:
        total += getNumOfPossibilities(i, numOfTimes - 1)
    total += getNumOfPossibilities(currentPos, numOfTimes - 1)

    dpTable[currentPos][numOfTimes] = total
    return  dpTable[currentPos][numOfTimes]



N = 5
for i in range(0, 10):
    getNumOfPossibilities(i, N)

allPossibilities=0
for i in range(0, 10):
    allPossibilities+=dpTable[i][N]

printDpTable()

print(allPossibilities)


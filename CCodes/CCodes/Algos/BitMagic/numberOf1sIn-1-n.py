#!/usr/bin/python
__author__ = 'serajago'

n = 32
maxBits = 64
count = [0] * maxBits

# count[i] - holds number of 1's in all the numbers that can be generated before setting i th bit as 1 plus 1
# number of 1's goes like this
'''
1   1
2   1
3   2
4   1
5   2
6   2
7   3
8   1
9   2
10  2
11  3
12  2
13  3
14  3
15  4
16  1
'''



def _getNumberOf1S():
    # base case
    count[0] = 1
    count[1] = 2
    for i in range(2, maxBits):
        count[i] = count[i - 1] + count[i - 1] + (pow(2, i - 1) - 1)


def getNumberOf1S(n):
    binary = bin(n)[2:]
    sumToBeAdded = 0
    total = 0
    for i in range(len(binary)):
        positionFromRight = len(binary) - i - 1
        numbersPossibleFromItoZero = pow(2, positionFromRight)
        if binary[i] == '1':
            total += count[positionFromRight] + sumToBeAdded * numbersPossibleFromItoZero
            sumToBeAdded += 1
    return total


_getNumberOf1S()
print(getNumberOf1S(7))

print(count)

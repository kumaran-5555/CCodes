#!/usr/bin/python
__author__ = 'serajago'

from Helpers.matrix import  Matrix


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

dpTable = Matrix(1, len(array))

# dpTable[i] is length of longest increase subarray ending with array[i]

def longestIncreasingSubarray():
    # base case
    dpTable[0] = 1
    for i in range(1, len(array)):
        if array[i-1] < array[i]:
            dpTable[i] = dpTable[i-1] + 1
        else:
            dpTable[i] = 1


longestIncreasingSubarray()
print(dpTable)





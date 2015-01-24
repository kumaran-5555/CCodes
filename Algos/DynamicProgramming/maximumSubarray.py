#!/usr/bin/python
__author__ = 'serajago'

from Helpers.matrix import  Matrix


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

dpTable = Matrix(1, len(array))

# dpTable[i] = holds the maximum sum of subarray with last element as array[i]

def maximumSubarray():
    # basecase
    dpTable[0] = array[0]

    for i in range(1, dpTable.cols):
        if dpTable[i-1]+ array[i] > array[i]:
            dpTable[i] = dpTable[i-1] + array[i]
        else:
            dpTable[i] = array[i]



maximumSubarray()
print(array)
print(dpTable)


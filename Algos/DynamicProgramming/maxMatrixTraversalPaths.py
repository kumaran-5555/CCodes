#!/usr/bin/python
__author__ = 'serajago'


# http://www.geeksforgeeks.org/count-possible-paths-top-left-bottom-right-nxm-matrix/

N = 3
M = 5

dpTable = []
for i in range(0, N):
    dpTable.append([0] * M)

# dpTable[i][j] holds the maximum number of traversal possible for matrix[0:i][0:j]

dpTable[0][0] = 1


def maxMatrixTraversalPath():
    for i in range(0, N):
        for j in range(0, M):
            if i == 0 and j == 0:
                dpTable[i][j] = 1
                continue

            fromAbovePath = 0
            if i > 0:
                fromAbovePath = dpTable[i - 1][j]
            fromLeftPath = 0
            if j > 0:
                fromLeftPath = dpTable[i][j - 1]

            dpTable[i][j] = fromAbovePath + fromLeftPath


maxMatrixTraversalPath()

for i in range(0, N):
    print(dpTable[i])






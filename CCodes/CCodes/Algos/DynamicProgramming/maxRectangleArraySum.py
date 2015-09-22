__author__ = 'serajago'

array = [[1, 2, -1, -4, -20],
         [-8, -3, 4, 2, 1],
         [3, 8, 10, 1, 3],
         [-4, -1, 1, 7, -6]]


N = len(array)
M = len(array[0])


startRow = []
startCol = []
maxVal = []

for i in range(N):
    maxVal.append([None]*M)
    startRow.append([-1]*M)
    startCol.append([-1]*M)



def maxSubMatrix():


    for i in range(N):
        for j in range(M):
            if i==0 and j==0:
                # base condition
                maxVal[0][0] = array[0][0]
                startRow[0][0] = 0
                startCol[0][0] = 0
            else:



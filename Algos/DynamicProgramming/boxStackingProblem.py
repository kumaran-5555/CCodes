__author__ = 'kumaran'

import Helpers.matrix

boxes = [[3,1,2],[6,4,5],[4,6,7],[32,10,12]]


dpTable = []

# dpTable[i] = holds the maximum height we can get with the stack ending with box i

def boxStacking():
    global dpTable
    allPossibleBoxes = []
    # dimension 0 - is width
    # dimesion 1 - is bredth
    # dimension 2 - is height
    # create all possible boxes
    for i in range(0,len(boxes)):
        allPossibleBoxes.append(boxes[i])
        b1 = [boxes[i][1], boxes[i][2], boxes[i][0]]
        b2 = [boxes[i][2], boxes[i][0], boxes[i][1]]
        allPossibleBoxes.append(b1)
        allPossibleBoxes.append(b2)

    allPossibleBoxes.sort(key=lambda x: x[0]*x[1], reverse=True)
    dpTable = Helpers.matrix.Matrix(rows=1, cols=len(allPossibleBoxes),defaultVal=0)


    # base case dpTable[0]
    dpTable[0] = allPossibleBoxes[0][2]
    n = len(allPossibleBoxes)
    for i in range(1, n):
        maxHeight = allPossibleBoxes[i][2]
        for j in range(0,i ):
            if allPossibleBoxes[j][0] > allPossibleBoxes[i][0] and allPossibleBoxes[j][1] > allPossibleBoxes[i][1]:
                # possible to stack j on i
                maxHeight = max(maxHeight, allPossibleBoxes[i][2] + dpTable[j])
        dpTable[i] = maxHeight


    print(allPossibleBoxes)
boxStacking()

print(dpTable)
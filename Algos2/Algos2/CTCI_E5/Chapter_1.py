import sys
from collections import defaultdict
import numpy




def stringHasAllUnique_1_1(s):
    
    charCount = defaultdict(int)

    for c in s:
        charCount[c] += 1

    for c in charCount:
        if charCount[c] > 1:
            return False

    return True




def isPermuation_1_3(s1, s2):

    charCount1 = defaultdict(int)

    for c in s1:
        charCount1[c] += 1

    charCount2 = defaultdict(int)

    for c in s2:
        charCount2[c] += 1


    for c in charCount1:
        if c not in charCount2 or charCount2[c] != charCount1[c]:
            return False


    return True



def stringCompression_1_5(s):

    compressedString = []

    prev = ''
    count = 0
    for c in s:

        if c != prev:
            if prev != '':
                # add to compressed 
                compressedString.append(str(count)+prev )
            count = 1
            
        else:
            count += 1

        prev = c

    if count > 0:
        compressedString.append(str(count) + prev)


    rVal = ''.join(compressedString)

    if len(rVal) < len(s):
        return rVal

    return s





def rotateArray_1_6(array):

    r,c = array.shape

    for i,j in zip(range(r), range(r)):

        r1 = i
        c1 = i
        while r1 < r:
            # swap 
            temp = array[i][c1]
            array[i][c1] =  array[r1][j]
            array[r1][j] = temp

            r1 += 1
            c1 += 1





def colsRowsZero_1_7(array):
    r,c = array.shape

    rowSatus = numpy.zeros((1,c))
    colStatus = numpy.zeros((1,c))

    for (i,j), in array.ndenumerate(array):
        if array[i,j] == 0:
            rowStatus[i] = 1
            colStatus[j] = 1


    for (i,j), in array.ndenumerate(array):
        if rowSatus[i] == 1 or colStatus[j] == 1:
            array[i,j] = 0



def containsAfterRotation_1_8(s1, s2):

    s2temp = s2 + s2

    if len(s1) == len(s2) and s1 in s2temp:
        return True

    return False





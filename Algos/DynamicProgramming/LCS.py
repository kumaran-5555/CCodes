__author__ = 'serajago'

import math

str1 = "AGGTAB"
str2 = "GXTXAYB"


def LCS(str1, str2):
    n = len(str1)
    m = len(str2)
    dpTable = []
    for i in range(0, n + 1):
        dpTable.append([0] * (m + 1))

    # LCS[i,j] provides, LCS of str1[:i] and str2[:j]

    # LCS of str1[:0] and str2[:j] is 0
    for i in range(0, m + 1):
        dpTable[0][i] = 0
    # LCS of str1[:i] and str[:0] is 0
    for i in range(0, n + 1):
        dpTable[i][0] = 0

    # update conditions
    # if str1[i] == str2[j],  LCS[i,j] = LCS[i-1,j-1] + 1
    # if str1[i] != str2[j],  LCS[i,j] = max(LCS[i-1,j], LCS[i,j-1])
    print(dpTable)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i-1] != str2[j-1]:
                dpTable[i][j] = max(dpTable[i - 1][j], dpTable[i][j - 1])
            else:
                dpTable[i][j] = dpTable[i - 1][j - 1] + 1

    for i in range(0, n + 1):
        print(dpTable[i])


LCS(str1, str2)





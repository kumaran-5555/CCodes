#!/usr/bin/python
__author__ = 'serajago'
# http://www.geeksforgeeks.org/dynamic-programming-set-36-cut-a-rope-to-maximize-product/'

N = 11

dpTable = [0] * ( N + 1)
# dpTable[i] of holds the maximum product achievable of rod length i
# assuming that cutting is optional
dpTable[0] = 0
dpTable[1] = 0


def maxProductCutting(length, isAlreadyCut):
    '''
    # special cases if cutting is mandatory
    if not isAlreadyCut:
        if length == 2:
            return 1
        elif length == 3:
            return 2
    '''
    if dpTable[length] != 0:
        return dpTable[length]

    # cut all i + length-i options and see which one yeids max
    maxProduct = 0
    for i in range(1, length):
        currProduct = maxProductCutting(i, True) * maxProductCutting(length - i, True)
        maxProduct = max(maxProduct, currProduct)

    if isAlreadyCut:
        maxProduct = max(maxProduct, length)

    dpTable[length] = maxProduct

    return maxProduct


print(maxProductCutting(N, False))
print(dpTable)



#!/usr/bin/python3
__author__ = 'kumaran'

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        l = len(num)
        d = {}
        for i in range(l):
            d[num[i]] = i+1

        for i in range(l):
            if target-num[i] in d:
                if d[target-num[i]] != i+1 and d[target-num[i]] > i+1:
                    return (i+1, d[target-num[i]])




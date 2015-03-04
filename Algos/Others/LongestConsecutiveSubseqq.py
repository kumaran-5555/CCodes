#!/usr/bin/python3
__author__ = 'kumaran'


class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        partialResult = {}
        maxLen = 0

        for i in num:
            # we have seen this number already, so can't increase our
            # result
            if i in partialResult:
                continue

            # check for left immediate
            if i-1 in partialResult:
                left = partialResult[i-1]
            else:
                left = 0

            # check for right immediate
            if i+1 in partialResult:
                right = partialResult[i+1]
            else:
                right = 0

            total = left + right + 1

            # update left and right
            if left:
                partialResult[i-left] = total

            if right:
                partialResult[i+right] = total

            # remember current to avoid double counting when it occurs again
            # if i is in middle, this only severs as binary flag
            # if i is either left or right end, it provides accumulated length
            partialResult[i] = total

            if maxLen < total:
                maxLen = total


        return  maxLen







if __name__ == '__main__':
    s = Solution()
    print(s.longestConsecutive([100,4,200,2,3,1]), 4)
    print(s.longestConsecutive([1]), 1)
    print(s.longestConsecutive([0,-1,1]), 3)
    print(s.longestConsecutive([0,-1]), 2)
    print(s.longestConsecutive([0,-1,1,2,3,8,9,10]), 5)

#!/usr/bin/python3
__author__ = 'kumaran'


class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        l = len(A)
        if not l or l == 1:
            return 0

        quantity = 0
        maxLr = [0] * l
        maxRl = [0] * l
        maxLr[0] = A[0]
        maxRl[-1] = A[-1]
        maxIdx = 0

        for i in range(1,l):
            if A[i] > maxLr[i-1]:
                maxLr[i] = A[i]
                maxIdx = i
            else:
                maxLr[i] = maxLr[i-1]
        for i in range(l-1-1,-1,-1):
            if A[i] > maxRl[i+1]:
                maxRl[i] = A[i]
            else:
                maxRl[i] = maxRl[i+1]

        curr = 0
        i = maxIdx
        while i < l-1:
            nextMax = maxRl[i+1]
            j = i+1
            while A[j] < nextMax:
                curr += (nextMax - A[j])
                j += 1

            quantity += curr
            curr = 0
            i = j

        i = maxIdx
        curr = 0
        while i > 0:
            nextMax = maxLr[i-1]
            j = i-1
            while A[j] < nextMax:
                curr += (nextMax - A[j])
                j -= 1

            quantity += curr
            curr = 0
            i = j

        return quantity







if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

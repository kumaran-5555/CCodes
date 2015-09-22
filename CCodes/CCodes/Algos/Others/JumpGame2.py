#!/usr/bin/python3
__author__ = 'kumaran'


class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        steps = 0
        l = len(A)

        if l == 1:
            return steps

        i = 0
        while i < l-1:

            # see if can reach the end from here
            if A[i] + i >= l-1:
                return steps + 1
            # if we can't move from here, return zero
            if A[i] == 0:
                return 0
            # iterate over the indicies that are possible
            # from here.
            # choose the one, that will take use farther
            maxVal = 0
            maxIdx = None
            for j in range(i+1, A[i]+i+1):
                if A[j] + j > maxVal:
                    maxVal = A[j] + j
                    maxIdx = j

            # we can't move from here, looks like
            # everything is zero
            if maxIdx is None:
                return 0

            steps += 1
            i = maxIdx


if __name__ == '__main__':
    s = Solution()
    

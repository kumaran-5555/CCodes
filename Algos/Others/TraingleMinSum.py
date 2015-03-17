#!/usr/bin/python3
__author__ = 'kumaran'


class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        l = len(triangle)
        # memory to store temp sum
        sumArray = []
        sumArray.append([float('inf')] * l)
        sumArray.append([float('inf')] * l)
        curr = 0
        if not l:
            assert 1==2

        sumArray[curr%2][0] = triangle[0][0]

        for i in range(1,l):
            for j in range(i+1):
                if j == 0:
                    # no previous
                    sumArray[(curr+1)%2][j] = sumArray[curr%2][j] + triangle[i][j]
                elif j == i:
                    # no current
                    sumArray[(curr+1)%2][j] = sumArray[curr%2][j-1] + triangle[i][j]
                else:
                    sumArray[(curr+1)%2][j] = min(sumArray[curr%2][j], sumArray[curr%2][j-1]) + triangle[i][j]

            curr += 1

        return min(sumArray[curr%2])



if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,18,8,1]
]))



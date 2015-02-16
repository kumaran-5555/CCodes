#!/usr/bin/python3

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]

    def binSearchLastNo(self, a, k):
        s = 0
        e = len(a)-1

        while s < e:
            mid = s + (e-s+1) // 2
            if a[mid] < k:
                s = mid
            else:
                e = mid - 1
        if a[s] < k:
            return s
        else:
            return -1

    def binSearchFirstYes(self, a, k):
        s = 0
        e = len(a)-1
        while s < e:
            mid = s + (e-s) // 2
            if a[mid] >= k:
                e = mid
            else:
                s = mid + 1

        if a[s] == k:
            return s
        else:
            return -1



    def searchRange(self, A, target):
        # find left range
        left = self.binSearchFirstYes(A, target)
        if left == -1:
            return [-1,-1]


        right = self.binSearchLastNo(A, target+1)

        return [left, right]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 5))


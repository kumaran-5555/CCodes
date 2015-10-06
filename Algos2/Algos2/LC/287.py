import math


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 1
        end = len(nums)-1

        n = len(nums)

        while start < end:

            mid = start + (end - start)//2

            leftCount = 0
            rightCount = 0

            for i in range(n):
                if nums[i] >= start and nums[i] <= mid:
                    leftCount += 1
                elif nums[i] > mid and nums[i] <= end:
                    rightCount += 1

            if leftCount > (mid - start + 1):
                # dups at left
                end = mid

            else:
                # dups at right
                start = mid+1




        return end


if __name__ == '__main__':
    s = Solution()
    s.findDuplicate([8,1,1,1,2,7,4,3,1,1])




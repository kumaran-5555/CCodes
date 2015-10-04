class Solution(object):

    def firstYes(self, nums, target, n):

        start = 0
        end = n-1

        while start < end:
            mid = start + (end - start)//2
            if nums[mid] >= target:
                end = mid

            else:
                start = mid + 1


        if nums[end] >= target:
            return end

        return -1


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        n = len(nums)

        # find left side
        left = self.firstYes(nums, target, n)

        if nums[left] != target:
            return [-1,-1]

        # find right
        right = self.firstYes(nums, target+1, n)

        if right == -1:
            return [left, n-1]

        return [left, right-1]


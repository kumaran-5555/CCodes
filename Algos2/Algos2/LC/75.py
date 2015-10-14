class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        nonZero = 0

        nonTwo = n-1

        while nonZero < nonTwo:
            while nums[nonZero] == 0:
                nonZero += 1

            while nums[nonTwo] == 2:
                nonTwo -= 1



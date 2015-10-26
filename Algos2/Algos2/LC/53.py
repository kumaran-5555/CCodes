class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        if n == 0:
            return 0

        rVal = nums[0]

        prev = nums[0]

        for i in range(1, n):
            if prev + nums[i] > nums[i]:
                prev += nums[i]

            else:
                prev = nums[i]


            if prev > rVal:
                rVal = prev

        return rVal



class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        if n == 0:
            return True


        
        currentReach = nums[0]

        for i in range(n):
            if i > currentReach:
                return False

            if nums[i] + i > currentReach:
                currentReach = nums[i] + i


        return True


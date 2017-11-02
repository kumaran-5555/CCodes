class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = [(i, nums[i]) for i in range(len(nums))]
        
        if len(nums) == 0:
            return 0
        
        nums = sorted(nums)        
        lis = 1
        lis_ = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i][1] >= prev[1] and nums[i][0] > prev[0]:
                lis_ += 1                
            else:
                lis = max(lis, lis_)
                lis_ = 1
                
            prev = nums[i]

        lis = max(lis, lis_)

        return lis

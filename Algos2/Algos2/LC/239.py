class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        n = len(nums)

        if n == 0:
            return []

        output = [0] * n
        output[n-1] = nums[n-1]
        i = n-1
        
        while i >= 0:
            x = nums[i]
            j = i+1
            while j > i - k and  nums[j] > nums[i]:
                output[j]  = nums[i]
                j -= 1

            i = j


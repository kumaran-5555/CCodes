

class Solution(object):
    def twoSums(self, nums, start, end, target):

        
        i = start
        j = end

        while i < j:
            sum = nums[i] + nums[j]

            if sum == target:
                self.result[(-target, nums[i], nums[j])] = 1
                i += 1
                j -= 1
            elif sum < target:
                i += 1

            else:
                j -= 1

        return None

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = {}
        nums = sorted(nums)

        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.twoSums(nums, i+1, n-1, 0-nums[i])

        return self.result.keys()

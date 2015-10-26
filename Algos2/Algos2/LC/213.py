class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n == 0:
            return 0
            
        if n == 1:
            return nums[0]
            
        dp1 = [0] * n

        for i in range(n-1):
            if i == 0:
                dp1[i] = nums[i]
            elif i == 1:                
                dp1[i] = max(nums[i], dp1[i-1])

            else:
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])


        rVal = dp1[n-2]

        for i in range(1,n):
            if i == 1:
                dp1[i] = nums[i]
            elif i == 2:                
                dp1[i] = max(nums[i], dp1[i-1])

            else:
                dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])

        return max(rVal, dp1[n-1])


if __name__ == '__main__':
    s = Solution()
    s.rob([1,2,3,4,5])







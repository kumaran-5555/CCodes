class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        x = []
        y = []
        if n == 0:
            return 0

        if n == 1:
            return nums[0]


        x.append(nums[0])
        y.append(0)

        x.append(y[0] + nums[1])
        y.append(x[0])



        

        for i in range(2, n):
            if y[i-1] + nums[i] > y[i-2] + nums[i]:
                x.append(y[i-1] + nums[i])
            else:
                x.append(y[i-2] + nums[i])

            if x[i-1] > x[i-2]:
                y.append(x[i-1])

            else:
                y.append(x[i-2])



        return max(x[n-1], y[n-1])




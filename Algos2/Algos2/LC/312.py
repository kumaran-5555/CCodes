class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        self.dp = []
        n = len(nums)
        if n == 0:
            return 0

        for i in range(n):
            self.dp.append([-1]*n)

        self.nums = [1] + nums + [1]

        return self.result(0, n-1)



    def result(self, s, e):
        if e < s:
            return 0

        # s, e are inclusive boundary
        if  self.dp[s][e] != -1:
            return self.dp[s][e]

        if s == e:
            self.dp[s][e] = self.nums[s-1] * self.nums[s] * self.nums[s+1]
            return self.dp[s][e]

        for i in range(s, e+1):
            a = self.result(s, i-1)
            b = self.result(i+1, e)

            result = a + b + self.nums[s-1] * self.nums[i] * self.nums[e+1]
            self.dp[s][e] = max(self.dp[s][e], result)


        return self.dp[s][e]


        

if __name__ == '__main__':
    c = Solution()
    print(c.maxCoins([3,1,5,8]))

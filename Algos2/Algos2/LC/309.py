class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        buy = 0
        sell = 1
        rest = 2
        n = len(prices)
        if n == 0:
            return 0
        dp = []
        dp.append([0]*n)
        dp.append([0]*n)
        dp.append([0]*n)

        for i in range(1, n):
            # buy should follow rest
            dp[buy][i] = max(dp[sell][i-1], dp[rest][i-1])
            dp[sell][i] = max(dp[buy][i-1], dp[buy][i-1]+ prices[i] - prices[i-1])
            dp[rest][i] = max(dp[sell][i-1], dp[rest][i-1])

        return max(dp[buy][n-1], dp[sell][n-1], dp[rest][n-1])
        
if __name__ == '__main__':
    c = Solution()
    print(c.maxProfit([6,1,3,2,4,7]))



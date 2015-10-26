class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)

        if n <= 1:
            return 0

        maxProfit = 0

        min = prices[0]

        for i in range(1,n):
            if min > prices[i]:
                min = prices[i]
            else:
                if maxProfit < prices[i] - min:
                    maxProfit = prices[i] - min
        return maxProfit


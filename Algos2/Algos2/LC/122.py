class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0

        n = len(prices)
        
        bought = - 1
        for i in range(n):
            # looking for valley
            if i > 0 and i < n-1 and prices[i-1] >= prices[i] < prices[i+1]:
                bought = prices[i]
            elif i ==0 and i < n-1 and prices[i+1] > prices[i]:
                bought = prices[i]

            # looking for peek
            if i > 0 and i < n-1 and prices[i-1] < prices[i] >= prices[i+1]:
                # for sure bought exists
                profit += prices[i] - bought
                bought = -1

            elif i > 0 and i == n-1 and prices[i-1] < prices[i]:
                profit += prices[i] - bought
                bought = -1

        return profit





if __name__ == '__main__':
    s = Solution()
    s.maxProfit([86,38,45,51])

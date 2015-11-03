class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        if n == 0:
            return 0

        s = [int(i) for i in list(s)]

        dp = [0] * (n+1)

        # we can always decode one digit
        for i in range(n+1):
            if i == 0:
                dp[i] = 0
                continue

            if i == 1:
                # we can always decode one digit
                dp[i] = 1
                continue

            prev =  dp[i-1] if s[i-1] > 0 else 0

            curr = dp[i-2] if s[i-1] <= 6 and s[i-2] <= 2 and s[i-2] > 0 else 0
            dp[i] = prev + curr

        return dp[n]



if __name__ == '__main__':
    s = Solution()
    s.numDecodings('2323')



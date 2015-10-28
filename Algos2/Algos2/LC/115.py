class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        dp = []

        n = len(s)
        m = len(t)

        for i in range(n+1):
            dp.append([0]*(m+1))

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0:
                    # empty source and empty target
                    dp[i][j] = 1
                    continue
                if i == 0:
                    # empty source and not-empty target
                    dp[i][j] = 0
                    continue

                if j == 0:
                    # empty target and non-empty source
                    dp[i][j] = 1

                    continue

                if s[i-1] == t[j-1]:
                    # dp[i][j] = we are able to match t[:j] with s[:i-1] + we are able to matcht[:j-1] with s[:i-1] 
                    dp[i][j] = (dp[i-1][j] + dp[i-1][j-1])

                else:
                    # dp[i][j] = we are able to match t[:j] with s[:i-1]
                    dp[i][j] = dp[i-1][j]

        return dp[n][m]

if __name__ == '__main__':
    s = Solution()
    s.numDistinct('aslkelfjhahasfsj', 'lhs')



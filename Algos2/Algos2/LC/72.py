class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        n = len(word1)
        m = len(word2)

        dp = []

        for i in range(n+1):
            dp.append([0]*(m+1))

        for i in range(n+1):
            for j in range(m+1):
                
                if i == 0:
                    dp[i][j] = j
                    continue
                if j == 0:
                    dp[i][j] = i
                    continue

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1

        return dp[n][m]


if __name__ == '__main__':
    s = Solution()
    s.minDistance('asdadfs', 'asdfsdf')




                


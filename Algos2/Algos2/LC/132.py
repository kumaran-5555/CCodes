class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        n = len(s)

        dp = []


        '''
        dp[i][j] = True if s[i:j+1] is palindrome
                 = dp[i+1][j-1] and s[i] == s[j]
        '''

        for i in range(n):
            dp.append([False]* (n))



        for k in range(1,n+1):
            for i in range(n):
                if k == 1:
                    # single char
                    dp[i][i+k-1] = True
                    continue

                if i+k-1 >= n:
                    # don't have enough chars
                    continue

                if k == 2:
                    if s[i] == s[i+1]:
                        dp[i][i+k-1] = True

                else:
                    dp[i][i+k-1] = dp[i+1][i+k-2] and s[i] == s[i+k-1]


        minCut = [n-1]*n

        minCut[0] = 0

        for i in range(1,n):
            cut = minCut[i-1]+1
            for j in range(i-1,-1,-1):
                if dp[j][i]:
                    if j > 0:
                        cut = min(minCut[j-1]+1, cut)
                    else:
                        cut = 0
            minCut[i] = cut

        return minCut[n-1]


                
                




        

if __name__ == '__main__':
    s = Solution()
    s.minCut('ahellollehworld')







                
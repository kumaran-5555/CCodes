class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        

        '''
            dp[i][j] = true if s1[:i], s2[:j] can create s3[:i+j] with interleving
                    =  false otherwise

            dp[i][j] = (dp[i-1][j] is True and s1[i] == s3[i+j]) or 
                        (dp[i][j-1] is True and s2[j] == s3[i+j])


        '''


        dp = []

        n = len(s1)
        m = len(s2)

        k = len(s3)

        if n+m != k:
            return False

        for i in range(n+1):
            dp.append([False]*m+1)

        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue

                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j-1+1]) or \
                            (dp[i][j-1] and s2[j-1] == s3[i-1+j-1+1])

        return dp[n][m]





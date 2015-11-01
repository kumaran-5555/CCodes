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
                if s[i-1] > 0:
                    # we can always decode one digit
                    dp[i] = 1
                    continue
                else:
                    return 0



            if s[i-1] > 0:
                prev =  dp[i-1]
            else:
                prev = 0

            if s[i-2] > 0 and s[i-2] * 10 + s[i-1] > 0 and s[i-2] * 10 + s[i-1] <= 26:
                if i == 2:
                    curr = 1
                else:
                    curr = dp[i-2]
            else:
                curr = 0


            
            
            dp[i] = prev + curr
            
            if dp[i] == 0:
                return 0


        return dp[n]



if __name__ == '__main__':
    s = Solution()
    s.numDecodings('232345')




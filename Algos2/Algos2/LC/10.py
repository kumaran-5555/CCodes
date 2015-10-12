class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)

        dpTable = []

        p = [''] + list(p)
        s = [''] + list(s)

        
        for i in range(m+1):
            dpTable.append([False]*(n+1))

        for i in range(m+1):
            for j in range(n+1):
                if i==0 and j == 0:
                    #empty pattern and empty string
                    dpTable[i][j] = True
                    continue

                if i == 0:
                    # empty pattern
                    dpTable[i][j] = False
                    continue



                if p[i] == '.' and j > 0:
                    dpTable[i][j] = dpTable[i-1][j-1]

                elif p[i] == '*':
                    if dpTable[i-1][j]:
                        # we just matched the prefix, i.e looking for only one instance
                        dpTable[i][j] = dpTable[i-1][j]
                    elif dpTable[i][j-1] and (p[i-1] == s[j] or p[i-1] == '.'):
                        # we matched both x* and we got one more x
                        dpTable[i][j] = True
                    elif i >= 2 and dpTable[i-2][j]:
                        # we don't need x* to match
                        dpTable[i][j] = True

                elif p[i] == s[j] and dpTable[i-1][j-1]:
                    dpTable[i][j] = True

        return dpTable[m][n]


if __name__ == '__main__':
    s = Solution()
    s.isMatch('a', '.*..a*')

    assert(s.isMatch('aab','c*a*b*') == True)
    assert(s.isMatch("aa","aa") == True)
    assert(s.isMatch("aaa","aa") == False)
    assert(s.isMatch("aa", "a*") == True)
    assert(s.isMatch("aa", ".*") == True)
    assert(s.isMatch("ab", ".*") == True)
    assert(s.isMatch("aab", "c*a*b") == True)



    



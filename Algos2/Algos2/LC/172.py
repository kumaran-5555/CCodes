class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        currentNumZeros = 0
        
        while n >= 5:
            i = 5
            currentNumZeros += 1
            while i * 5 <= n:
                currentNumZeros += i
                i *= 5
                
            n -= i
        
        
        
        return currentNumZeros

if __name__ == '__main__':
    s = Solution()
    s.trailingZeroes(126)



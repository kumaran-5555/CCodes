class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        isNegative = n < 0

        n = abs(n)


        self.parital = [1, x]
                
        for i in range(2,32):
            self.parital.append(self.parital[i-1] * self.parital[i-1])

        rval = 1
        mask = 1
        for i in range(1,32):
            if mask & n:
                rval *= self.parital[i]
            mask <<= 1
    
        if isNegative:
            return 1/rval

        return rval



if __name__ == '__main__':
    s = Solution()
    s.myPow(0.5,0)


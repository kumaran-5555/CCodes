import math
class Solution(object):
    def f(self, n, x):
        return  n - x ** 2

    def fDash(self, n, x):
        return -2*x


    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        curr = float(x) / 2

        while True:
        
            next = curr - self.f(x, curr) / self.fDash(x, curr)    

            if abs(next-curr) < 0.01:
                return int(next)

            curr = next



if __name__ == '__main__':
    s = Solution()
    s.mySqrt(10)


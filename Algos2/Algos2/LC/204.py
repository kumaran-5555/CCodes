import math

class Solution(object):





    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        

        
        rVal = [1] * n
        rVal[0] = 0
        rVal[1] = 0
        

        for i in range(2, n//2):

            if rVal[i] == 1:
                j = 2
                while j*i < n:
                    rVal[i*j] = 0


        return sum(rVal)









        
if __name__ == '__main__':
    s = Solution()
    s.countPrimes(999983)

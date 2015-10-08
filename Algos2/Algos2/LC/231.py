class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # if number 1 bits is 1, it is power of 2

        count = 0
        if n < 0:
            return False
        while n:
            count += 1

            n &= (n-1)

        if count == 1:
            return True

        return False

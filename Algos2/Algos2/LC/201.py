class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        diff = n - m

        output = 0
        for i in range(32):
            p = 1 << i
            if diff >= p:
                continue

            output |= ((m & p) & (n & p))

        return output


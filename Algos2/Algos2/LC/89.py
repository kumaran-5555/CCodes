class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        count = [0] * n
        sign = [1] * n

        num = 0

        i = 0

        output = []
        while i < 2**n:
            
            for j in range(n):
                mask = 1 << j
                if i % (1 << (j+1)) == 1<<j:
                    if num & mask:
                        num &= ~mask
                    else:
                        num |= mask
                                        
            output.append(num)
            i += 1






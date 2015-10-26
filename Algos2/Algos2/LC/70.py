class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2
        i_2 = 1
        i_1 = 2

        for i in range(2,n):
            next = i_1 + i_2

            i_2 = i_1
            i_1 = next


        return 





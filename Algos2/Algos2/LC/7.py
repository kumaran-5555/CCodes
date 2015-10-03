class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)

        num = 0

        i = 10
        while y > 0:
            num = num * 10 + y % 10
            y = y // 10


        if num >= 2**31:
            return 0

        if x < 0:
            return -num

        return num

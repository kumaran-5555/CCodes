class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num - (9 * (num - 1)// 9)



        
        
        
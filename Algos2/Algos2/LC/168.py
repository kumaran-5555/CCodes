class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        mapping = {}

        start = ord('A')
        end = ord('Z')
        for i in range(start, end):
            mapping[i-start+1] = chr(i)

        mapping[0] = 'Z'


        output = ''
        while n:
            output = mapping[n % 26] + output

            n = (n-1)//26

        return output


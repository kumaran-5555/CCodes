class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = ord('A')
        end = ord('Z')

        mapping = {}

        for i in range(start, end+1):
            mapping[chr(i)] = i-start+1

        rVal = 0

        multiplier = 1

        n = len(s)

        for i in range(n-1, -1, -1):
            rVal += (mapping[s[i]] * multiplier)

            multiplier *= 26


        return rVal



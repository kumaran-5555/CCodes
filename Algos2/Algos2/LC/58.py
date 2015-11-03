class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        lastWordLen = 0

        currWordLen = 0
        for c in s:
            if c != ' ':
                currWordLen += 1
            elif currWordLen > 0:
                lastWordLen = currWordLen
                currWordLen = 0


        if currWordLen > 0:
            return currWordLen

        return lastWordLen
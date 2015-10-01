class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charsDict = {}

        longestString = 0

        currLeft = 0
        n = len(s)
        for i in range(n):
            c = s[i]
            if c in charsDict:
                # we have seen this char already 
                # if c is in currentWindow, update
                # otherwise continue
                if charsDict[c] >= currLeft:
                    currLeft = charsDict[c]+1
            if longestString < i - currLeft +1:
                longestString = i - currLeft + 1

            charsDict[c] = i

        return longestString
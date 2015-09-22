__author__ = 'kumaran'

class Solution:

    def maxMatcing(self, c1, c2, string, l):
        # c1 - left cursor
        # c2 - right cursor
        matchedLen = 0
        while c1 >=0 and c2 < l:
            if string[c1] == string[c2]:
                matchedLen += 1
                c1 -= 1
                c2 += 1
            else:
                break
        #print(c1,c2,matchedLen)
        return  matchedLen

    def longestPalindrome(self, string):
        l = len(string)
        if not l:
            return None
        maxLen = 1
        startIdx = 0
        endIdx = 0

        for i in range(l):
            # look for even palindrome
            if i < l-1:

                pLen = self.maxMatcing(i,i+1,string,l)
                if pLen * 2 > maxLen:
                    maxLen = pLen * 2
                    startIdx = i-pLen+1
                    endIdx = i + pLen
            # look for odd palindrome
            if i > 0 and i < l-1:
                pLen = self.maxMatcing(i-1,i+1, string, l)
                if (pLen * 2) + 1 > maxLen:
                    maxLen = (pLen * 2) + 1
                    startIdx = i-pLen
                    endIdx = i+pLen

        #print(maxLen)
        return string[startIdx:endIdx+1]

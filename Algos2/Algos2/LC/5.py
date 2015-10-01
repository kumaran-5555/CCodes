class Solution(object):


    def longestEven(self, s, i):
        n = len(s)
        j = i-1
        longest = 0
        while j >= 0 and i < n:
            if s[j] == s[i]:
                j -= 1 
                i += 1
            else:
                break

        return j+1, i-j-1

    def longestOdd(self, s, i):
        n = len(s)
        j = i-1
        k = i+1

        while j >=0  and k < n:
            if s[j] == s[k]:
                j -= 1
                k += 1
            else:
                break


        return j+1, k-j-1



    




                
                
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        longest = 0
        start = -1

        n = len(s)


        for i in range(n):
            even, evenLen = self.longestEven(s,i)
            odd, oddLen = self.longestOdd(s,i)

            if evenLen > longest:
                start = even
                longest = evenLen

            if oddLen > longest:
                start = odd
                longest = oddLen






            

        return s[start:start+longest]

          









        
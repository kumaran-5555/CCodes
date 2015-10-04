class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        s = '1'

        n -=1 

        while n:
            newS = []

            m = len(s)
            j = 0
            while j < m:
                count = 1
                char = s[j]
                while j+1 < m and s[j] == s[j+1]:
                    count += 1
                    j += 1
                newS.append(str(count)+char)

                j += 1

            n -= 1
            s = ''.join(newS)




        return s
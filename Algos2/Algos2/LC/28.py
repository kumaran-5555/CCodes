class Solution(object):

    def hash(self, s, start, end):
        prime = 101
        h = 0

        while start <= end:
            h += prime * ord(s[start])
            start += 1


        return h



    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        n = len(haystack)
        m = len(needle)

        if n == 0 and m == 0:
            return 0

        if m > n:
            return -1

        if m == 0:
            return 0

        hH = self.hash(haystack, 0, m-1)
        hN = self.hash(needle, 0, m-1)

        for i in range(n-(m-1)):
            if hH == hN:
                if haystack[i:i+m] == needle:
                    return i

            # update hash

            if i + m < n:
                new = ord(haystack[i+m])  * 101
                old = ord(haystack[i]) * 101
                hH += new
                hH -= old

            else:
                break

        return -1


if __name__ == '__main__':
    s = Solution()
    s.strStr('a','a')

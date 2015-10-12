class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        n = len(s)
        s = s.lower()

        if n == 0:
            return True

        i = 0
        j = n-1

        while i < j:
            if not str.isalnum(str(s[i])):
                i += 1
            elif not str.isalnum(str(s[j])):
                j -= 1

            elif s[i] != s[j]:
                return False

            else:
                i += 1
                j -= 1

        return True


if __name__ == '__main__':
    s = Solution()

    s.isPalindrome("A man, a plan, a canal: Panama")



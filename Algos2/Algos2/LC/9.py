class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False

        maxPosition = 1

        temp = x
        while temp // 10 :
            temp = temp // 10
            maxPosition *= 10

        minPosition = 10

        big = x
        small = x
        while maxPosition >= minPosition:
            if big // maxPosition == small % minPosition:
                big = big % maxPosition
                small = small // minPosition
                maxPosition = maxPosition // 10
            else:
                return False

        if maxPosition < minPosition:
            return True

        return False




if __name__ == '__main__':
    s = Solution()
    s.isPalindrome(0)

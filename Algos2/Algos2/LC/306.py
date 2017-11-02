class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        for i in range(1, n-1):
            if num.startswith("0") and i > 1:
                break

            for j in range(i+1, n):
                n1 = int(num[:i])
                n2 = int(num[i:j])
                if num[i:].startswith('0') and j > i+1:
                    break
                    

                if self._isAdditiveNumber(n1, n2, num[j:]):
                    return True

        return False

        

    def _isAdditiveNumber(self, n1, n2, num):
        sum = n1 + n2
        if num == '':
            return True

        if not num.startswith(str(sum)):
            return False

        if num.startswith("0") and sum > 0:
            return False

        num = num[len(str(sum)):]
        return self._isAdditiveNumber(n2, sum, num)

if __name__ == '__main__':
    c = Solution()
    c.isAdditiveNumber("1023")
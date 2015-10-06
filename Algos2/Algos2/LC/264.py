class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        output = [0] * n

        output[0] = 1


        prev2 = 0
        prev5 = 0
        prev3 = 0

        j = 1

        while j < n:
            next2 = output[prev2] * 2
            next3 = output[prev3] * 3
            next5 = output[prev5] * 5

            minVal = None

            if next2 <= next3 and next2 <= next5:
                minVal = next2
            elif next3 <= next5:
                minVal = next3
            else:
                minVal = next5


            if minVal == next2:
                output[j] = next2
                prev2 += 1

            if minVal == next3:
                output[j] = next3
                prev3 += 1

            if minVal == next5:
                output[j] = next5
                prev5 += 1

            j += 1

        return output[-1]



if __name__ == '__main__':
    s  = Solution()
    s.nthUglyNumber(10)

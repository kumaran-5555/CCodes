class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        rVal = float('-inf')

        negativeLeft = 0
        negativeRight = 0

        n = len(nums)

        if n == 0:
            return 0



        temp = 0
        l = 0

        for i in nums:
            if i == 0:

                if l == 1:
                    max = temp
                
                elif temp < 0:
                    # reset
                    # compute max of previous range and update
                    if negativeLeft >= negativeRight and negativeLeft != 0:
                        max = temp / negativeLeft

                    elif negativeRight > negativeLeft and negativeRight != 0:
                        max = temp / negativeRight

                else:
                    max = temp

                if max > rVal:
                    rVal = max
                    
                if rVal < 0:
                    rVal = 0
                
                l = 0

                negativeLeft = 0
                negativeRight = 0
                temp = 0

            elif i > 0:

                if temp == 0:
                    temp = i
                else:
                    temp *= i

                l += 1

                if negativeRight != 0:
                    negativeRight *= i

            else:
                if temp == 0:
                    temp = i

                else:
                    temp *= i

                l += 1
                if negativeLeft == 0:
                    negativeLeft = temp

                negativeRight = i

        if l == 1:
            max = temp

        elif temp < 0:
            # reset
            # compute max of previous range and update
            if negativeLeft >= negativeRight and negativeLeft != 0:
                max = temp / negativeLeft

            elif negativeRight > negativeLeft and negativeRight != 0:
                max = temp / negativeRight

        else:
            max = temp

        if max > rVal:
            rVal = max


        return rVal

if __name__ == '__main__':
    s = Solution()
    s.maxProduct([-4,-3,-2])


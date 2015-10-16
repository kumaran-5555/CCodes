class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)

        if n == 1:
            return 0

        currentSteps = 0
        if nums[0] >= n-1:
            return 1


        position = 0

        while position < n:

            if nums[position] + position >= n-1:
                return currentSteps + 1

            nextPosition = nums[position] + position
            
            currentRange = nums[nextPosition] + nextPosition

            

            # we can't reach from here to last, definitel at least 2 hops                            
            for j in range(position, nextPosition + 1):
                if nums[j] + j >= n-1:
                    return currentSteps + 2

                
                if currentRange < nums[j] + j:
                    currentRange = nums[j] + j
                    nextPosition = j


            position = nextPosition
            currentSteps += 1

        return currentSteps


if __name__ == '__main__':
    s = Solution()
    s.jump([7,8,4,2,0,6,4,1,8,7,1,7,4,1,4,1,2,8])





                



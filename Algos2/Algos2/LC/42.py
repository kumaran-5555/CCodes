class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        

        stack = []

        n = len(height)

        if n == 0:
            return 0

        total = 0

        stack.append((height[0],0))
        leftMax = height[0]


        for i in range(1,n):
            if stack[-1][0] >= height[i]:
                stack.append((height[i], i))

            else:
                while len(stack) > 1 and stack[-1][0] <= height[i]:
                    total += ((min(height[i], stack[-2][0]) - stack[-1][0]) * (i - stack[-2][1] - 1))

                    stack.pop()

                if len(stack) == 1 and stack[-1][0] < height[i]:
                    # stack has the left end of the wall, remove it and 
                    # current as the left wall

                    stack.pop()


                stack.append((height[i],i))



        return total



if __name__ == '__main__':
    s = Solution()
    s.trap([0,1,0,2,1,0,1,3,2,1,2,1])

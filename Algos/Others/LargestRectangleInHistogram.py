#!/usr/bin/python3
__author__ = 'kumaran'


class Solution():
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        l = len(height)
        if not l:
            return 0

        widthL = [0] * l
        widthR = [0] * l
        stack = []

        # for each column compute the max rectangle having height as big as it

        stack.append([height[0],0])
        for i in range(1,l):
            currHeight = height[i]
            # check if current element is bigger than previous
            while len(stack) and stack[-1][0] > currHeight:
                # if it is smaller, the rectagle having previous as max height,
                # can't cotinue here
                temp = stack.pop()
                widthR[temp[1]] = i-temp[1]-1
            stack.append([height[i],i])

        while len(stack):
            temp = stack.pop()
            widthR[temp[1]] = l-1-temp[1]

        stack.append([height[-1],l-1])

        for i in range(l-1-1,-1,-1):
            currHeight = height[i]
            while len(stack) and stack[-1][0] > currHeight:
                temp = stack.pop()
                widthL[temp[1]] = temp[1]-i-1
            stack.append([height[i],i])

        while len(stack):
            temp = stack.pop()
            widthL[temp[1]] = temp[1]-0

        maxArea = 0
        for i in range(l):
            area = height[i] * (1+ widthR[i]+widthL[i])
            if area >maxArea:
                maxArea = area


        return maxArea








if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2,1,2]))
    #print(s.largestRectangleArea([2,1,5,6,2,3]))

